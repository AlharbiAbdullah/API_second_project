from pydantic import BaseModel


# Blog Schema model 
class Blog(BaseModel):
    title: str
    body: str

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

# What data to show to the end user 
class ShowUser(BaseModel):
    name: str 
    email: str
    class Config():
        orm_mode = True

