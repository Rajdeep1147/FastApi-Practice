from fastapi import FastAPI,Depends, HTTPException,status,Response
from sqlalchemy.orm import Session
from schemas import *
from model import *
from database import *
from hashing import Hash
from typing import List
from routers.blog import router
from routers.users import router as users_router


app = FastAPI()
app.include_router(router)
app.include_router(users_router)
Base.metadata.create_all(bind=engine)
