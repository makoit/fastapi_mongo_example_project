from pydantic import BaseModel, Field
from typing import Optional


class Admin(BaseModel):
    username: str = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "fullname": "admin",
            }
        }


class AdminInConfig(Admin):
    hashed_password: str = Field(...)
