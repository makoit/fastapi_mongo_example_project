# functions to change id format between db level and application level
from bson.objectid import ObjectId
from typing import Union
from config.config import DB


def change_id_format_to_db(student):
    student["_id"] = str(student["id"])
    return student

def change_id_format_to_basic(student):
    student["id"] = str(student["_id"])
    return student

# raise custom exception instead of none
def validate_object_id(id: str) -> Union[str,None]:
    try:
        _id = ObjectId(id)
    except:
        return None

    return _id

# raise custom exception instead of none
async def get_student_or_none(id: str):
    id = validate_object_id(id)
    if id:
        student = await DB.student_collection.find_one({"_id": ObjectId(id)})
        if student:
            return student
        else:
            return None
    else:
        return None