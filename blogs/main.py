from fastapi import (FastAPI , Depends , status ,
                     Response) 
from . import schemas, models
from .database import engine , get_db
from sqlalchemy.orm import Session

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
@app.get('/blog')
def get_blogs(db: Session = Depends(get_db)):
    blogs = db.query(models.Blog).all()
    return {
        'blogs' : blogs
    }

# get a blog by ID 
@app.get('/blog/{id}' , status_code= status.HTTP_200_OK)
def get_blog(id , response: Response, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {
            'details' : f"blog with ID {id} doesn't exists"
        }
    return {
        f'blog for ID {id}' : blog
    }

