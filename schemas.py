from pydantic import BaseModel
from typing import List

class BlogBase(BaseModel):
    name: str
    description: str    
    body: str
    class Config:
        from_attributes = True


class BlogCreate(BlogBase):
    pass

class Blog(BlogBase):
    user_id: int
    class Config:
        from_attributes = True
    

class UserBase(BaseModel):
    name: str
    email: str
    password: str

class showUser(BaseModel):
    name: str
    email: str
    blogs: list[Blog] = []
    class Config:
        from_attributes = True


class showBlog(BlogBase):
    id: int
    user_id: int
    class Config:
        from_attributes = True

class CreateUser(UserBase):
    pass

class user(UserBase):
    id: int
    class Config:
        from_attributes = True

class Login(BaseModel):
    email: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: str | None = None    