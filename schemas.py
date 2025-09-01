from pydantic import BaseModel

class BlogBase(BaseModel):
    name: str
    description: str
    body: str

class BlogCreate(BlogBase):
    pass

class showBlog(BlogBase):
    name: str
    description: str    
    body: str

class Blog(BlogBase):
    id: int
    
    class Config:
        from_attributes = True

class UserBase(BaseModel):
    name: str
    email: str
    password: str

class showUser(BaseModel):
    name: str
    email: str

class CreateUser(UserBase):
    pass

class user(UserBase):
    id: int
    class Config:
        from_attributes = True