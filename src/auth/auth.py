from config.config import ADMIN_CONFIG, TOKEN_SECRET_KEY, ALGORITHM
from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from fastapi import Depends, HTTPException, status, APIRouter
from typing import Optional
from pydantic import BaseModel
from jose import JWTError, jwt
from datetime import datetime, timedelta
from models.token import Token, TokenData


auth_router = APIRouter()

# Utilities

# context to hash and verify passwords
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# enable oauth2 password schema
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# compare plain password and hashed password in db


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


# create new access token if user is authentiacted


def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, TOKEN_SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def validate_access_token(token: str = Depends(oauth2_scheme)):

    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    try:
        payload = jwt.decode(token, TOKEN_SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = TokenData(username=username)
    except JWTError:
        raise credentials_exception
    if token_data.username != ADMIN_CONFIG.username:
        raise credentials_exception
    return ADMIN_CONFIG
