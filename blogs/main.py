from fastapi import FastAPI , Depends
from . import schemas, models
from .database import engine , get_db
from sqlalchemy.orm import Session


app = FastAPI()

models.Base.metadata.create_all(engine)

@app.post('/blog')
def create(request: schemas.Blog , db: Session = Depends(get_db)):
    new_blog = models.Blog(title=request.title , 
                            body=request.body)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return {
        'new blog created' : new_blog
    }