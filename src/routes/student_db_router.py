# imports
from fastapi import APIRouter, Depends, HTTPException, status, Body
from typing import List

# student db controller
from database import student_controller
# models
from models.student import StudentModel, UpdateStudentModel
from models.student_db import StudentOnDbModel

# middleware
from .student_middleware import object_id_check, student_available_check

# create instance of APIRouter (mini fastapi instance)
db_student_router = APIRouter()

# create instance of student controller
db_student_access = student_controller.StudentDbAccess()


# create new student in db
@db_student_router.post(
    "/",
    response_model=StudentOnDbModel,
    status_code=status.HTTP_201_CREATED
)
async def create_student(student: StudentModel = Body(...)):
    """[summary]
    Inserts a new student to DB.

    [description]
    Endpoint to add a new student.
    """

    new_student = await db_student_access.create_new_student(student.dict())

    if new_student:
        return new_student
    else:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Student could not created")


# read all students from db
@db_student_router.get(
    "/",
    response_model=List[StudentOnDbModel],
    status_code=status.HTTP_200_OK
)
async def get_all_students(limit: int = 50, skip: int = 0):
    """[summary]
        Gets all students.

       [description]
        Endpoint to retrieve students from DB.
    """

    students = await db_student_access.read_all_students(limit, skip)

    if not students:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="No students found")
    else:
        return students


# read a student from db by id
@db_student_router.get(
    "/{id}",
    dependencies=[Depends(object_id_check), Depends(student_available_check)],
    response_model=StudentOnDbModel,
    status_code=status.HTTP_200_OK
)
async def get_student_by_id(id: str):
    """[summary]
    Get one student by ID.

    [description]
    Endpoint to retrieve an specific student.
    """
    student = await db_student_access.read_student(id)
    return student


# update a student by id
@db_student_router.put(
    "/{id}",
    dependencies=[Depends(object_id_check), Depends(student_available_check)],
    response_model=StudentOnDbModel,
    status_code=status.HTTP_200_OK
)
async def update_student(id: str, student_data: StudentModel):
    """[summary]
    Update a student by id.

    [description]
    Endpoint to update an specific student with all fields.
    """
    student = await db_student_access.update_student(id, student_data.dict())

    if student:
        return student
    else:
        raise HTTPException(
            status_code=status.HTTP_304_NOT_MODIFIED, detail="Student not modified")


# partial update a student by id
@db_student_router.patch(
    "/{id}",
    dependencies=[Depends(object_id_check), Depends(student_available_check)],
    response_model=StudentOnDbModel,
    status_code=status.HTTP_200_OK
)
async def partial_update_student(id: str, student_data: UpdateStudentModel):
    """[summary]
    Partial update a student by id.

    [description]
    Endpoint to update an specific student with some or all fields.
    """
    student_data = {k: v for k, v in student_data.dict().items()
                    if v is not None}
    student = await db_student_access.update_student(id, student_data)

    if student:
        return student
    else:
        raise HTTPException(
            status_code=status.HTTP_304_NOT_MODIFIED, detail="Student not modified")


# delete a workshop by id from db -> missed response model
@db_student_router.delete(
    "/{id}",
    dependencies=[Depends(object_id_check), Depends(student_available_check)],
    status_code=status.HTTP_200_OK
)
async def delete_workshop_by_id(id: str):
    """[summary]
    Delete one student by ID.

    [description]
    Endpoint to delete an specific student.
    """

    delete_response = await db_student_access.delete_student(id)
    if delete_response:
        return delete_response
    else:
        raise HTTPException(
            status_code=status.HTTP_304_NOT_MODIFIED, detail="Student not deleted")
