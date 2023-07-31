from typing import List
from fastapi import APIRouter,Depends,status,HTTPException
import  database,schemas,models
from sqlalchemy.orm import Session
from hashing  import Hash
from fastapi.encoders import jsonable_encoder
from repository import user as user_repo

router=APIRouter(
    prefix="/user",
    tags=['Users']
)
get_db=database.get_db

#user creation
@router.post('/')
def create_user(request:schemas.User,db:Session =Depends(get_db)):
    return user_repo.create(request,db)
 
 
@router.get('/',response_model=List[schemas.ShowUser])
def get_user(db:Session =Depends(get_db)):
    return user_repo.get_all_user(db)


@router.get('/{id}',response_model=schemas.ShowUser)
def get_user(id:int,db:Session =Depends(get_db)):
    return user_repo.show(id,db)