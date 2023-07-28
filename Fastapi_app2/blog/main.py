from fastapi import FastAPI,Depends,status,Response,HTTPException
from fastapi.responses import Response,JSONResponse
from typing import Optional,List
import schemas,models
from database import engine,SessionLocal,get_db
from sqlalchemy.orm import Session
from hashing import Hash
from fastapi.encoders import jsonable_encoder
from routers import blog,user

app=FastAPI()

models.Base.metadata.create_all(engine)

# def get_db():
#     db=SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()


#---->comment added  up to last(uncomment this using :select all-->ctrl+?)

# # @app.post('/blog',status_code=201)
# @app.post('/blog/{current_user_id}',status_code=status.HTTP_201_CREATED,tags=['Blogs'])
# def create(current_user_id:int,request:schemas.Blog,db:Session =Depends(get_db)):
#     new_blog=models.Blog(title=request.title,body=request.body,user_id=current_user_id)
#     db.add(new_blog)
#     db.commit()
#     db.refresh(new_blog)
#     return new_blog

# @app.delete('/blog/{id}',status_code=status.HTTP_204_NO_CONTENT,tags=['Blogs'])
# def destroy(id,db:Session=Depends(get_db)):
#     blog=db.query(models.Blog).filter(models.Blog.id == id)
#     if not blog.first():
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Blog with id {id} not found")
#     blog.delete(synchronize_session=False)
#     db.commit()
#     return JSONResponse(content={"response": "Delete successfully done"},status_code=status.HTTP_200_OK)


# @app.put('/blog/{id}',status_code=status.HTTP_202_ACCEPTED,tags=['Blogs'])
# def update_blog(id,request:schemas.Blog,db:Session =Depends(get_db)):
#     blog=db.query(models.Blog).filter(models.Blog.id == id)
#     if not blog.first():
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Blog with id {id} not found")
#     blog.update(dict(request))
#     db.commit()
#     return JSONResponse(content={"response": f"Blog with id {id} Updated Successfully"},status_code=status.HTTP_200_OK)

# @app.get('/blog',response_model=List[schemas.ShowBlog],tags=['Blogs'])
# def fetch_all_blog(db:Session =Depends(get_db)):
#     blogs=db.query(models.Blog).all()
#     return blogs

# #using below line we can exclude id from response
# # @app.get('/blog/{id}',status_code=200,response_model=schemas.ShowBlog,response_model_exclude=["id"],tags=['Blogs'])
# @app.get('/blog/{id}',status_code=200,response_model=schemas.ShowBlog,tags=['Blogs'])
# def show(id:int,response:Response,db:Session =Depends(get_db)):
#     blog=db.query(models.Blog).filter(models.Blog.id==id).first()
#     if not blog:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'Blog with id {id} is not available')
#         #or...we can write as below 2 line
#         # response.status_code = status.HTTP_404_NOT_FOUND
#         # return {'detail':f'Blog with id {id} is not available'}
    
#     return blog
    


# #user creation

# @app.post('/user',tags=['User'])
# def create_user(request:schemas.User,db:Session =Depends(get_db)):
#      new_user = models.User(name=request.name,email=request.email,password=Hash.bcrypt(request.password))  #create a  new user
#      db.add(new_user)  #save the user in database
#      db.commit()
#      db.refresh(new_user)
#      return new_user
 
 
# @app.get('/user',response_model=List[schemas.ShowUser],tags=['User'])
# def get_user(db:Session =Depends(get_db)):
#     users=db.query(models.User).all()
#     user_data = jsonable_encoder(users)
#     return user_data


# @app.get('/user/{id}',response_model=schemas.ShowUser,tags=['User'])
# def get_user(id:int,db:Session =Depends(get_db)):
#     users=db.query(models.User).filter(models.User.id ==id).first()
#     if not users:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'User with id {id} does not exist')
#     # Convert the User object to a JSON serializable representation --->either use this or directly return users
#     # user_data = jsonable_encoder(users)
#     # return user_data
#     return users



app.include_router(blog.router)
app.include_router(user.router)