from database import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

class Blog(Base):
    __tablename__ = "blog"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String, index=True)
    body = Column(String, index=True)
    user_id = Column(Integer,ForeignKey("user.id"))
      # Use class name "User" instead of "users"
    creater = relationship("User", back_populates="blogs")

class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)   
    blogs = relationship("Blog", back_populates="creater")
