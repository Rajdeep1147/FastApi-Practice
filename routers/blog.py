from fastapi import APIRouter
from fastapi import Depends, HTTPException, status, Response
from sqlalchemy.orm import Session
from schemas import showBlog, BlogCreate
from model import Blog
from database import get_db    
from typing import List
from repository.blog import *

router = APIRouter(
    prefix="/blog",
    tags=["Blogs"],
)

@router.get('/',response_model=list[showBlog])
def get_blogs(db: Session = Depends(get_db)):
    return get_all_blogs(db)


#get blog by id
@router.get('/{id}',response_model=showBlog,status_code=200)
def get_blog(id: int, db: Session = Depends(get_db)):
    return get_single_blog(id, db)

#create blog
@router.post('/create_blog', response_model=showBlog)
def create_blog(request: BlogCreate, db: Session = Depends(get_db)):
   return create_new_blog(request, db)

#update blog
@router.put('/update_blog/{id}')
def update_blog(id: int, request: BlogCreate, db: Session = Depends(get_db)):
    return update_existing_blog(id, request, db)

#delete blog
@router.delete('/delete_blog/{id}',status_code=status.HTTP_204_NO_CONTENT,)
def delete_blog(id:int ,db:Session=Depends(get_db)):
   return delete_blog(id, db) 