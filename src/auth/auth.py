from passlib.context import CryptContext
from pydantic import BaseModel

# context to hash and verify passwords
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


# compare plain password and hashed password from config
def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password):
    return pwd_context.hash(password)

# auth user


def authenticate_user(user, username: str, password: str):

    if user.username != username:
        return False
    if not verify_password(password, user.hashed_password):
        return False
    return user
