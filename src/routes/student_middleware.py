from bson.objectid import ObjectId
from config.config import DB, CONF
from fastapi import HTTPException, status
import logging
from typing import Union

from database import db_helper

# check if id_ is a valid ObjectId 
# ObjectId is a 12-byte ObjectId value (with special value sequence)
# mongo driver generate at document store phase a unique _id field that acts as a primary key
def object_id_check(id: str) -> Union[str, HTTPException]:

    checked_id = db_helper.validate_object_id(id)
    if checked_id:
        return checked_id
    else:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="ID is not valid")

    # try:
    #     db_helper.validate_object_id(id)
    # except Exception:
    #     if CONF["fastapi"].get("debug", False):
    #         logging.warning("Invalid Object ID")
    #     raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="ID is not valid")
    # return _id


# validation if id is valid and if workshop is available in db
async def student_available_check(id: str):
    
    student = await db_helper.get_student_or_none(id)
    if student:
        return student
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Student not found")
