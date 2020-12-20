from jose import JWTError, jwt
from typing import Optional
from datetime import datetime, timedelta
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from config.config import ADMIN_CONFIG, TOKEN_SETTINGS
from models.token import Token, TokenData

# enable oauth2 password schema
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# create new access token if user is authentiacted


def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(
        to_encode, TOKEN_SETTINGS.TOKEN_SECRET_KEY, algorithm=TOKEN_SETTINGS.ALGORITHM)
    return encoded_jwt


def validate_access_token(token: str = Depends(oauth2_scheme)):

    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    try:
        payload = jwt.decode(token, TOKEN_SETTINGS.TOKEN_SECRET_KEY, algorithms=[
                             TOKEN_SETTINGS.ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = TokenData(username=username)
    except JWTError:
        raise credentials_exception
    if token_data.username != ADMIN_CONFIG.username:
        raise credentials_exception
    return ADMIN_CONFIG
