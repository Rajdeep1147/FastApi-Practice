from fastapi import APIRouter
from fastapi import Depends, HTTPException, status, Response
from sqlalchemy.orm import Session
from schemas import showBlog, BlogCreate
from model import Blog, User
from database import get_db    
from typing import List
from repository.blog import *
from Oath2 import get_current_user

router = APIRouter(
    prefix="/blog",
    tags=["Blogs"],
)

@router.get('/',response_model=list[showBlog])
def get_blogs(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return get_all_blogs(db)


#get blog by id
@router.get('/{id}',response_model=showBlog,status_code=200)
def get_blog(id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return get_single_blog(id, db, current_user)

#create blog
@router.post('/create_blog', response_model=showBlog)
def create_blog(request: BlogCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
   return create_new_blog(request, db, current_user)

#update blog
@router.put('/update_blog/{id}')
def update_blog(id: int, request: BlogCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return update_existing_blog(id, request, db, current_user)

#delete blog
@router.delete('/delete_blog/{id}',status_code=status.HTTP_204_NO_CONTENT,)
def delete_blog(id:int ,db:Session=Depends(get_db), current_user: User = Depends(get_current_user)):
   return delete_blog(id, db, current_user) 