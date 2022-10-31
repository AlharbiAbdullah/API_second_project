from typing import List
from fastapi import ( APIRouter , Depends ,status , 
                        HTTPException , Response ) 
from sqlalchemy.orm import Session 
from blogs import schemas , models, oauth2 
from blogs.database import get_db 
from blogs.repository  import blog


router = APIRouter(
    prefix= '/blog' , 
    tags=['blogs']
) 


# get blogs 
@router.get('', response_model= List[schemas.ShowBlog])
def get_blogs(db: Session = Depends(get_db)
            , current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.get_all(db)

# get a blog by ID 
@router.get('/{id}' , status_code= status.HTTP_200_OK, response_model=schemas.ShowBlog)
def get_blog(id , db: Session = Depends(get_db) , 
            current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.get_by_id(id, db)

# post new blogs 
@router.post('', status_code= status.HTTP_201_CREATED)
def create(request: schemas.Blog , db: Session = Depends(get_db), 
            current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.create(request, db) 

# Delete a blog 
@router.delete('/{id}' , status_code= status.HTTP_204_NO_CONTENT)
def deletion(id , db: Session = Depends(get_db), 
            current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.deletion(id, db) 


# Update a blog 
@router.put('/{id}', status_code= status.HTTP_202_ACCEPTED)
def update(id , request: schemas.Blog , db: Session = Depends(get_db), 
            current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.update(id , db) 

