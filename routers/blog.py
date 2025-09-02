from fastapi import APIRouter
from fastapi import Depends, HTTPException, status, Response
from sqlalchemy.orm import Session
from schemas import showBlog, BlogCreate
from model import Blog
from database import get_db    
from typing import List

router = APIRouter()

@router.get('/blogs',response_model=list[showBlog],tags=["blogs"])
def get_blogs(db: Session = Depends(get_db)):
    blogs = db.query(Blog).all()
    return blogs


#get blog by id
@router.get('/blogs/{id}',response_model=showBlog,status_code=200,tags=["blogs"])
def get_blog(id: int, db: Session = Depends(get_db)):
    blog = db.query(Blog).filter(Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code=404, detail=f"Blog {id} not found")
    return blog

#create blog
@router.post('/create_blog', response_model=showBlog, tags=["blogs"])
def create_blog(request: BlogCreate, db: Session = Depends(get_db)):
    new_blog = Blog(name=request.name, description=request.description, body=request.body, user_id=1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

#update blog
@router.put('/update_blog/{id}',tags=["blogs"])
def update_blog(id: int, request: BlogCreate, db: Session = Depends(get_db)):
    blog = db.query(Blog).filter(Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code=404, detail=f"Blog {id} not found")
    
    blog.name = request.name
    blog.description = request.description
    blog.body = request.body
    
    db.commit()
    db.refresh(blog)
    return blog    

#delete blog
@router.delete('/delete_blog/{id}',status_code=status.HTTP_204_NO_CONTENT,tags=["blogs"])
def delete_blog(id:int ,db:Session=Depends(get_db)):
    delete_blog = db.query(Blog).filter(Blog.id==id)
    if not delete_blog.first():
        raise HTTPException(status_code=404,detail=f"Blog {id} not found")
    delete_blog.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)    