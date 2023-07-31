from sqlalchemy.orm import Session
import models,schemas
from hashing import Hash
from fastapi.encoders import jsonable_encoder
from fastapi import HTTPException,status


def create(request:schemas.User,db:Session):
    new_user = models.User(name=request.name,email=request.email,password=Hash.bcrypt(request.password))  #create a  new user
    db.add(new_user)  #save the user in database
    db.commit()
    db.refresh(new_user)
    return new_user

def get_all_user(db:Session):
    users=db.query(models.User).all()
    user_data = jsonable_encoder(users)
    return user_data 

def show(id:int,db:Session):
    users=db.query(models.User).filter(models.User.id ==id).first()
    if not users:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'User with id {id} does not exist')
    # Convert the User object to a JSON serializable representation --->either use this or directly return users
    # user_data = jsonable_encoder(users)
    # return user_data
    return users
    