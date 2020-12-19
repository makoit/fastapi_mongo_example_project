# imports
from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from config import config
#from fastapi.security import OAuth2PasswordBearer

# routers
from routes.student_db_router import db_student_router
from routes.auth_router import auth_router

# auth
#oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
from auth.auth import validate_access_token


# create app instance
app = FastAPI(
    title="API documentation for app",
    description="This documentation defines how to access REST API of app",
    version="1.0.0",
    # dependencies=[Depends(oauth2_scheme)]
)

# define origins for CORS
origins = [
    "http://localhost:8080",
    "http://127.0.0.1:8080"
]

# allow access from specific origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# include router auth
app.include_router(
    auth_router,
    tags=["endpoints for auth"]
)

# include router for db access (mongo)
app.include_router(
    db_student_router,
    prefix="/students",
    tags=["endpoints for student db"],
    dependencies=[Depends(validate_access_token)],
    responses={404: {"description": "Not found"}},
)


# app startup event
@ app.on_event("startup")
async def app_startup():
    """
    Do tasks related to app initialization.
    """
    config.load_config()


# app shutdown event
@ app.on_event("shutdown")
async def app_shutdown():
    """
    Do tasks related to app termination.
    """
    config.close_db_client()
