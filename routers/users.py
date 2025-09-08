from fastapi import APIRouter, Depends, HTTPException
from schemas import showUser, CreateUser
from model import User
from database import get_db
from hashing import Hash
from sqlalchemy.orm import Session
from repository.user import *
from Oath2 import get_current_user

router = APIRouter(
    prefix="/users",
    tags=["Users"],
)


#create user
@router.post('/create_user',response_model=showUser)
def create_user(request:CreateUser,db:Session=Depends(get_db),current_user: User = Depends(get_current_user)):
   return createUser(request, db)

#get user by id
@router.get('/{id}', response_model=showUser)
def get_user(id: int, db: Session = Depends(get_db),current_user: User = Depends(get_current_user)):
   return getUserById(id, db)

#get all users
@router.get('/', response_model=list[showUser])
def get_all_users(db: Session = Depends(get_db),current_user: User = Depends(get_current_user)):
    users = db.query(User).all()
    return users


#delete user
@router.delete('/user_delete/{id}',response_model=showUser)
def delete_user(id:int,db:Session=Depends(get_db),current_user: User = Depends(get_current_user)):
   return deleteUser(id, db)