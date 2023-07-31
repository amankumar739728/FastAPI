from sqlalchemy.orm import Session
import models,schemas
from fastapi import HTTPException,status
from fastapi.responses import JSONResponse
from models import Blog



def get_all(db:Session):
    blogs=db.query(models.Blog).all()
    return blogs

def create(current_user_id:int,request:schemas.Blog,db:Session):
    new_blog=models.Blog(title=request.title,body=request.body,user_id=current_user_id)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

def show(id:int,db:Session):
    blog=db.query(models.Blog).filter(models.Blog.id==id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'Blog with id {id} is not available')
        #or...we can write as below 2 line
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return {'detail':f'Blog with id {id} is not available'}
    
    return blog

def update_blog(id:int,request:schemas.Blog,db:Session):
    blog=db.query(Blog).filter(Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Blog with id {id} not found")
    #Update the blog attributes with the values from the request
    blog.title = request.title
    blog.body = request.body
    db.commit()
    db.refresh(blog)
    return JSONResponse(content={"response": f"Blog with id {id} Updated Successfully"},status_code=status.HTTP_200_OK)


def destroy(id:int,db:Session):
    blog=db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Blog with id {id} not found")
    blog.delete(synchronize_session=False)
    db.commit()
    return JSONResponse(content={"response": "Delete successfully done"},status_code=status.HTTP_200_OK)