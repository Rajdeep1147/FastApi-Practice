from fastapi import APIRouter
from fastapi import Depends, HTTPException
from schemas import CreateUser
from model import User
from database import get_db
from hashing import Hash
from sqlalchemy.orm import Session
from repository.user import *
from sqlalchemy.orm import Session
from model import Blog
from database import get_db
from typing import List

def createUser(request:CreateUser,db:Session=Depends(get_db)):
    new_user=User(name=request.name,email=request.email,password=Hash.bcrypt(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def getUserById(id:int,db:Session=Depends(get_db)):
    user=db.query(User).filter(User.id==id).first()
    if not user:
        raise HTTPException(status_code=404,detail=f"User {id} not found")
    return user

def deleteUser(id:int,db:Session=Depends(get_db)):
    delete_user = db.query(User).filter(User.id==id).first()
    if not delete_user:
        raise HTTPException(status_code = 404, detail=f"User {id} not found")