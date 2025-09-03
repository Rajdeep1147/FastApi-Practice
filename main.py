from fastapi import FastAPI
from schemas import *
from model import *
from database import *
from routers.blog import router
from routers.users import router as users_router


app = FastAPI()
app.include_router(router)
app.include_router(users_router)
Base.metadata.create_all(bind=engine)
