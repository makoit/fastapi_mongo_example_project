# imports
from pydantic import BaseModel, EmailStr, Field
from typing import List, Optional
from datetime import datetime


class StudentModel(BaseModel):
    """[summary]
        Base user model.

        [description]
        Used to for user attributes.
    """

    fullname: str = Field(...)
    email: EmailStr = Field(...)
    course_of_study: str = Field(...)
    year: int = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "fullname": "Max Mustermann",
                "email": "max-muster@uni.com",
                "course_of_study": "IT",
                "year": 2
            }
        }


class UpdateStudentModel(BaseModel):
    """[summary]
        Model to update user.

        [description]
        Used to update user attributes.
    """

    fullname: Optional[str]
    email: Optional[EmailStr]
    course_of_study: Optional[str]
    year: Optional[int]

    class Config:
        schema_extra = {
            "example": {
                "fullname": "Max Maier",
                "email": "max_mainer@uni.com",
                "course_of_study": "Mechanical Engineering",
                "year": 4
            }
        }
