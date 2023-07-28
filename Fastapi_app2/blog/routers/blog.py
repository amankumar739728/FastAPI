from fastapi import FastAPI,Depends,status,Response,HTTPException,APIRouter
from fastapi.responses import Response,JSONResponse
from typing import Optional,List
import schemas,models,database
from database import engine,SessionLocal,get_db
from sqlalchemy.orm import Session
from fastapi.encoders import jsonable_encoder


router=APIRouter()
get_db=database.get_db





@router.get('/blog',response_model=List[schemas.ShowBlog],tags=['Blogs'])
def fetch_all_blog(db:Session =Depends(get_db)):
    blogs=db.query(models.Blog).all()
    return blogs


# @app.post('/blog',status_code=201)
@router.post('/blog/{current_user_id}',status_code=status.HTTP_201_CREATED,tags=['Blogs'])
def create(current_user_id:int,request:schemas.Blog,db:Session =Depends(get_db)):
    new_blog=models.Blog(title=request.title,body=request.body,user_id=current_user_id)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


#using below line we can exclude id from response
# @app.get('/blog/{id}',status_code=200,response_model=schemas.ShowBlog,response_model_exclude=["id"],tags=['Blogs'])
@router.get('/blog/{id}',status_code=200,response_model=schemas.ShowBlog,tags=['Blogs'])
def show(id:int,db:Session =Depends(get_db)):
    blog=db.query(models.Blog).filter(models.Blog.id==id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'Blog with id {id} is not available')
        #or...we can write as below 2 line
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return {'detail':f'Blog with id {id} is not available'}
    
    return blog


# @app.post('/blog',status_code=201)
@router.post('/blog/{current_user_id}',status_code=status.HTTP_201_CREATED,tags=['Blogs'])
def create(current_user_id:int,request:schemas.Blog,db:Session =Depends(get_db)):
    new_blog=models.Blog(title=request.title,body=request.body,user_id=current_user_id)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


@router.put('/blog/{id}',status_code=status.HTTP_202_ACCEPTED,tags=['Blogs'])
def update_blog(id,request:schemas.Blog,db:Session =Depends(get_db)):
    blog=db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Blog with id {id} not found")
    blog.update(dict(request))
    db.commit()
    return JSONResponse(content={"response": f"Blog with id {id} Updated Successfully"},status_code=status.HTTP_200_OK)

@router.delete('/blog/{id}',status_code=status.HTTP_204_NO_CONTENT,tags=['Blogs'])
def destroy(id,db:Session=Depends(get_db)):
    blog=db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Blog with id {id} not found")
    blog.delete(synchronize_session=False)
    db.commit()
    return JSONResponse(content={"response": "Delete successfully done"},status_code=status.HTTP_200_OK)