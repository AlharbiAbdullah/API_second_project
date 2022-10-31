from sqlalchemy.orm import Session 
from blogs import models , schemas 
from fastapi import HTTPException, status


# Get function 
def get_all(db: Session):
    blogs = db.query(models.Blog).all()
    return blogs

# Get by id function 
def get_by_id(id: int, db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, 
                            detail=f"Record with the ID {id} doesn't exists")
    return blog


# Create function
def create (request: schemas.Blog , db: Session):
    new_blog = models.Blog(title=request.title , 
                            body=request.body, 
                            user_id = 1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

# Delete function 
def deletion(id: int , db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, 
                            detail=f"Record with the ID {id} doesn't exists")
    blog.delete(synchronize_session=False)
    db.commit()
    return {
        f'Record for ID {id} has been deleted'
    }

# Update function 
def update(id: int, db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND,
                            detail=f"Record with the ID {id} doesn't exists")
    blog.update(request.dict())
    db.commit()
    return {
        f'Record with the ID {id} has been updated'
    }