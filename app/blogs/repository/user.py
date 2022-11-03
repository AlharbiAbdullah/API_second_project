from sqlalchemy.orm import Session 
from blogs import models , schemas, hashing
from fastapi import HTTPException, status

# Get user by ID 
def get_user_by_id(id: int , db: Session):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, 
                            detail=f"Record with the ID {id} doesn't exists")
    return user

# create a user 
def create(request: schemas.User, db: Session):
    new_user = models.User(name = request.name , 
                           email= request.email , 
                           password= hashing.Hash.bcrypt(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

