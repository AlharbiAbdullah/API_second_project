from sqlalchemy import Column , Integer , String 
from .database import Base

# blog table
class Blog(Base):
    __tablename__ = 'blogs'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    body = Column(String)

# user table 
class User(Base):
    __tablename__ = 'Users'
    
    id = Column(Integer , primary_key= True , index= True)
    name = Column(String) 
    email = Column(String) 
    password = Column(String) 
