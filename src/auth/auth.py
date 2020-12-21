from passlib.context import CryptContext
from pydantic import BaseModel
from models.admin import AdminInConfig


class AuthUser:

    def __init__(self):
        # context to hash and verify passwords
        self.pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

    # compare plain password and hashed password from config

    def verify_password(self, plain_password: str, hashed_password: str):
        return self.pwd_context.verify(plain_password, hashed_password)

    # auth user

    def authenticate_user(self, user: AdminInConfig, username: str, password: str):

        if user.username != username:
            return False
        if not self.verify_password(password, user.hashed_password):
            return False
        return user
