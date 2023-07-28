from typing import List
from fastapi import APIRouter,Depends,status,HTTPException
import  database,schemas,models
from sqlalchemy.orm import Session
from hashing  import Hash
from fastapi.encoders import jsonable_encoder

router=APIRouter()
get_db=database.get_db

#user creation
@router.post('/user',tags=['User'])
def create_user(request:schemas.User,db:Session =Depends(get_db)):
     new_user = models.User(name=request.name,email=request.email,password=Hash.bcrypt(request.password))  #create a  new user
     db.add(new_user)  #save the user in database
     db.commit()
     db.refresh(new_user)
     return new_user
 
 
@router.get('/user',response_model=List[schemas.ShowUser],tags=['User'])
def get_user(db:Session =Depends(get_db)):
    users=db.query(models.User).all()
    user_data = jsonable_encoder(users)
    return user_data


@router.get('/user/{id}',response_model=schemas.ShowUser,tags=['User'])
def get_user(id:int,db:Session =Depends(get_db)):
    users=db.query(models.User).filter(models.User.id ==id).first()
    if not users:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'User with id {id} does not exist')
    # Convert the User object to a JSON serializable representation --->either use this or directly return users
    # user_data = jsonable_encoder(users)
    # return user_data
    return users