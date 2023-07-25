from fastapi import FastAPI,Depends,status,Response,HTTPException
from fastapi.responses import Response,JSONResponse
from typing import Optional
import schemas,models
from database import engine,SessionLocal
from sqlalchemy.orm import Session

app=FastAPI()

models.Base.metadata.create_all(engine)

def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()


# @app.post('/blog',status_code=201)
@app.post('/blog',status_code=status.HTTP_201_CREATED)
def create(request:schemas.Blog,db:Session =Depends(get_db)):
    new_blog=models.Blog(title=request.title,body=request.body)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

@app.delete('/blog/{id}',status_code=status.HTTP_204_NO_CONTENT)
def destroy(id,db:Session=Depends(get_db)):
    db.query(models.Blog).filter(models.Blog.id == id).delete(synchronize_session=False)
    db.commit()
    return JSONResponse(content={"response": "Delete successfully done"},status_code=status.HTTP_200_OK)


@app.put('/blog/update/{id}',status_code=status.HTTP_201_CREATED)
def update_blog(id,request:schemas.Blog,db:Session =Depends(get_db)):
    blog=db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Blog with id {id} not found")
    blog.update(request)
    db.commit()
    return JSONResponse(content={"response": "Blog Updated Successfully"},status_code=status.HTTP_200_OK)

@app.get('/blog')
def fetch_all_blog(db:Session =Depends(get_db)):
    blogs=db.query(models.Blog).all()
    return blogs

@app.get('/blog/{id}',status_code=200)
def show(id,response:Response,db:Session =Depends(get_db)):
    blog=db.query(models.Blog).filter(models.Blog.id==id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'Blog with id {id} is not available')
        #or...we can write as below 2 line
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return {'detail':f'Blog with id {id} is not available'}
    
    return blog

#1:31:49/4:02:55 ----> Link:https://www.youtube.com/watch?v=7t2alSnE2-I&ab_channel=Bitfumes