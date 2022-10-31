from pydantic import BaseModel
from typing import List


# Blog Schema model 
class Blog(BaseModel):
    title: str
    body: str
    
    class Config():
        orm_mode = True

# creating a class to decide what to show to the consumer 
# we need to extend the blog model 
class ShowBlog(Blog):
    class Config():
        orm_mode = True

# User schema model 
class User(BaseModel):
    name: str 
    email: str 
    password: str

    class Config():
        orm_mode = True



# What data to show to the end user 
class ShowUser(BaseModel):
    name: str 
    email: str
    blogs: List[Blog] = []

    class Config():
        orm_mode = True

# creating a class to decide what to show to the consumer 
# we need to extend the blog model 
class ShowBlog(Blog):
    title: str 
    body: str 
    creator: ShowUser

    class Config():
        orm_mode = True

