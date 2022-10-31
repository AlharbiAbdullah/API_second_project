from fastapi import ( APIRouter , Depends ,status , 
                        HTTPException ) 
from sqlalchemy.orm import Session 
from blogs import schemas , models , hashing
from blogs.database import get_db
from blogs.repository import user 


router = APIRouter(
    prefix= '/user' , 
    tags=['users']
) 


# Creating a user 
@router.post('' , status_code= status.HTTP_201_CREATED, response_model=schemas.ShowUser)
def create_user(request: schemas.User, db: Session = Depends(get_db)):
    return user.create(request , db) 

# Get user by ID 
@router.get('/{id}', status_code= status.HTTP_200_OK, response_model=schemas.ShowUser)
def get_user(id: int,  db: Session = Depends(get_db)):
    return user.get_user_by_id(id , db)
