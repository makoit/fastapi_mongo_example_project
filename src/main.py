# imports
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from config import config

# routers
from routes.student_db_router import db_student_router


#create app instance
app = FastAPI(    
    title="API documentation for app",
    description="This documentation defines how to access REST API of app",
    version="1.0.0",
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


# include router for db access (mongo)
app.include_router(
    db_student_router,
    prefix="/student",
    tags=["endpoints for student db"],
    responses={404: {"description": "Not found"}},
)


# app startup event 
@app.on_event("startup")
async def app_startup():
    """
    Do tasks related to app initialization.
    """
    config.load_config()


# app shutdown event
@app.on_event("shutdown")
async def app_shutdown():
    """
    Do tasks related to app termination.
    """
    config.close_db_client()
