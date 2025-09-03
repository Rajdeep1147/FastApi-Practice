from fastapi import APIRouter
from fastapi import Depends, HTTPException, status, Response
from sqlalchemy.orm import Session
from schemas import showBlog, BlogCreate
from model import Blog
from database import get_db
from typing import List

def get_all_blogs(db:Session()=Depends(get_db)):
    blogs = db.query(Blog).all()
    return blogs

def get_single_blog(id:int, db:Session=Depends(get_db)):
    blog = db.query(Blog).filter(Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code=404, detail=f"Blog {id} not found")
    return blog

def create_new_blog(request:BlogCreate, db:Session=Depends(get_db)):
    new_blog = Blog(name=request.name, description=request.description, body=request.body, user_id=1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

def update_existing_blog(id:int, request:BlogCreate, db:Session=Depends(get_db)):
    blog = db.query(Blog).filter(Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code=404, detail=f"Blog {id} not found")
    
    blog.name = request.name
    blog.description = request.description
    blog.body = request.body
    
    db.commit()
    db.refresh(blog)
    return blog    

def delete_blog(id:int, db:Session=Depends(get_db)):
    delete_blog = db.query(Blog).filter(Blog.id==id)
    if not delete_blog.first():
        raise HTTPException(status_code=404,detail=f"Blog {id} not found")
    delete_blog.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)   