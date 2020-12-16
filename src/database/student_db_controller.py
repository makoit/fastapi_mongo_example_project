from bson import ObjectId
from config.config import DB
from .db_helper import change_id_format_to_db, change_id_format_to_basic, get_student_or_none
from typing import Union, List

# models
from models.student import StudentModel, UpdateStudentModel
from models.student_db import StudentOnDbModel


class StudentDbAccess:

    """ Class implementing CRUD operations on student collection in MongoDB """

    def __init__(self):
        self.database_client = DB

    async def read_all_students(self, limit: int = 50, skip: int = 0) -> Union[List[StudentOnDbModel], None]:

        student_cursor = self.database_client.student_collection.find().skip(skip).limit(limit)
        students = await student_cursor.to_list(length=limit)

        if not students:
            return None
        else:
            return list(map(change_id_format_to_basic, students))

    async def read_student(self, id: str) -> StudentOnDbModel:

        student = await self.database_client.student_collection.find_one({"_id": ObjectId(id)})
        return change_id_format_to_basic(student)

    async def delete_student(self, id: str) -> Union[dict, None]:

        student_op = await self.database_client.student_collection.delete_one({"_id": ObjectId(id)})

        if student_op.deleted_count:
            return {"status": f"deleted count: {student_op.deleted_count}"}
        else:
            return None

    async def update_student(self, id: str, student_data: dict) -> Union[StudentOnDbModel, None]:

        if len(student_data) < 1:
            return None

        student_op = await self.database_client.student_collection.update_one(
            {"_id": ObjectId(id)}, {"$set": student_data}
        )

        if student_op.modified_count:
            updated_student = await self.read_student(id)
            return change_id_format_to_basic(updated_student)
        else:
            return None

    async def create_new_student(self, student_data: dict) -> Union[StudentOnDbModel, None]:

        student_op = await self.database_client.student_collection.insert_one(student_data)

        if student_op.inserted_id:
            new_student = await get_student_or_none(student_op.inserted_id)
            if new_student:
                return change_id_format_to_basic(new_student)
            else:
                return None
        else:
            return None
