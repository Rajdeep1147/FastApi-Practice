from fastapi import APIRouter, Depends, HTTPException
from schemas import showUser, CreateUser
from model import User
from database import get_db
from hashing import Hash
from sqlalchemy.orm import Session

router = APIRouter()

#create user
@router.post('/create_user',response_model=showUser,tags=["users"])
def create_user(request:CreateUser,db:Session=Depends(get_db)):
    new_user=User(name=request.name,email=request.email,password=Hash.bcrypt(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

#get user by id
@router.get('/users/{id}', response_model=showUser, tags=["users"])
def get_user(id: int, db: Session = Depends(get_db)):
    user = db.query(User).get(id)
    if not user:
        raise HTTPException(status_code=404, detail=f"User {id} not found")
    return user

#get all users
@router.get('/get_all_users',response_model=list[showUser],tags=["users"])
def get_all_users(db:Session=Depends(get_db)):
    users = db.query(User).all()
    return users

#delete user
@router.delete('/user_delete/{id}',response_model=showUser,tags=["users"])
def delete_user(id:int,db:Session=Depends(get_db)):
    delete_user = db.query(User).filter(User.id==id).first()
    if not delete_user:
        raise HTTPException(status_code = 404, detail=f"User {id} not found")