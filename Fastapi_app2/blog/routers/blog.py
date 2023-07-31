from fastapi import FastAPI,Depends,status,Response,HTTPException,APIRouter
from fastapi.responses import Response,JSONResponse
from typing import Optional,List
import schemas,models,database,oauth2
from database import engine,SessionLocal,get_db
from sqlalchemy.orm import Session
from fastapi.encoders import jsonable_encoder
from repository import blog as blog_repo  # Rename the imported module to blog_repo


#in case of any doubt please refer blog folder main.py file commented code.

#to make the code clean we use router concepts(i.e prefix and tags)
router=APIRouter(
    prefix="/blog", #prefix used to make the url endpoint short --->in decorator we use short url.
    tags=['Blogs']  #writing all the tags at one place:otherwise in @app.get('/',tags=['Blogs']) we need to write again & again
)


get_db=database.get_db





@router.get('/',response_model=List[schemas.ShowBlog])
def fetch_all_blog(db:Session =Depends(get_db),current_user:schemas.User=Depends(oauth2.get_current_user)):
    return blog_repo.get_all(db)    #from repository blog is imported


# @app.post('/blog',status_code=201)
@router.post('/{current_user_id}',status_code=status.HTTP_201_CREATED)
def create(current_user_id:int,request:schemas.Blog,db:Session =Depends(get_db),current_user:schemas.User=Depends(oauth2.get_current_user)):
   return blog_repo.create(current_user_id,request,db)


#using below line we can exclude id from response
# @app.get('/blog/{id}',status_code=200,response_model=schemas.ShowBlog,response_model_exclude=["id"],tags=['Blogs'])
@router.get('/{id}',status_code=200,response_model=schemas.ShowBlog)
def show(id:int,db:Session =Depends(get_db),current_user:schemas.User=Depends(oauth2.get_current_user)):
   return blog_repo.show(id,db)


@router.put('/{id}',status_code=status.HTTP_202_ACCEPTED)
def update_blog(id:int,request:schemas.Blog,db:Session =Depends(get_db),current_user:schemas.User=Depends(oauth2.get_current_user)):
    return blog_repo.update_blog(id,request,db)

@router.delete('/{id}',status_code=status.HTTP_204_NO_CONTENT)
def destroy(id:int,db:Session=Depends(get_db),current_user:schemas.User=Depends(oauth2.get_current_user)):
    return blog_repo.destroy(id,db)