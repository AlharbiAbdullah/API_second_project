from fastapi import (FastAPI , Depends , status ,
                     Response, HTTPException) 
from . import schemas, models, hashing
from .database import engine , get_db
from sqlalchemy.orm import Session
from typing import List

# creating the app 
app = FastAPI()

# creating database schemas and tables.
models.Base.metadata.create_all(engine)

# post new blogs 
@app.post('/blog', status_code= status.HTTP_201_CREATED)
def create(request: schemas.Blog , db: Session = Depends(get_db)):
    new_blog = models.Blog(title=request.title , 
                            body=request.body)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return {
        'new blog created' : new_blog
    }

# get blogs 
@app.get('/blog', response_model= List[schemas.ShowBlog])
def get_blogs(db: Session = Depends(get_db)):
    blogs = db.query(models.Blog).all()
    return blogs

# get a blog by ID 
@app.get('/blog/{id}' , status_code= status.HTTP_200_OK, response_model=schemas.ShowBlog)
def get_blog(id , response: Response, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, 
                            detail=f"Record with the ID {id} doesn't exists")
    return blog

# Delete a blog 
@app.delete('/blog/{id}' , status_code= status.HTTP_204_NO_CONTENT)
def deletion(id , db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, 
                            detail=f"Record with the ID {id} doesn't exists")
    blog.delete(synchronize_session=False)
    db.commit()
    return {
        f'Record for ID {id} has been deleted'
    }

# Update a blog 
@app.put('/blog/{id}', status_code= status.HTTP_202_ACCEPTED)
def update(id , request: schemas.Blog , db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND,
                            detail=f"Record with the ID {id} doesn't exists")
    blog.update(request.dict())
    db.commit()
    return {
        f'Record with the ID {id} has been updated'
    }

# Creating a user 
@app.post('/user',status_code= status.HTTP_201_CREATED)
def create_user(request: schemas.User, db: Session = Depends(get_db)):
    new_user = models.User(name = request.name , 
                           email= request.email , 
                           password= hashing.Hash.bcrypt(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

