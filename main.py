from fastapi import FastAPI,Depends, HTTPException,status,Response
from sqlalchemy.orm import Session
from schemas import *
from model import *
from database import *
from hashing import Hash




app = FastAPI()
Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def index():
    return {'message': 'Hello, World!'}


@app.post('/create_blog')
def create_blog(request: BlogCreate, db: Session = Depends(get_db)):
    new_blog = Blog(name=request.name, description=request.description, body=request.body)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


@app.get('/blogs',response_model=list[showBlog])
def get_blogs(db: Session = Depends(get_db)):
    blogs = db.query(Blog).all()
    return blogs

@app.get('/blogs/{id}',status_code=200)
def get_blog(id: int, db: Session = Depends(get_db)):
    blog = db.query(Blog).filter(Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code=404, detail=f"Blog {id} not found")
    return blog

@app.put('/update_blog/{id}')
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

@app.delete('/delete_blog/{id}',status_code=status.HTTP_204_NO_CONTENT)
def delete_blog(id:int ,db:Session=Depends(get_db)):
    delete_blog = db.query(Blog).filter(Blog.id==id)
    if not delete_blog.first():
        raise HTTPException(status_code=404,detail=f"Blog {id} not found")
    delete_blog.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)

@app.post('/create_user',response_model=showUser)
def create_user(request:CreateUser,db:Session=Depends(get_db)):
    new_user=User(name=request.name,email=request.email,password=Hash.bcrypt(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user