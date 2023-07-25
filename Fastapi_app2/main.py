from fastapi import FastAPI,Path
from pydantic import BaseModel
from typing import Optional
from pdb import set_trace as breakpoint
import uvicorn

app=FastAPI()

# students={
#     1:{
#         "name":"Aman",
#         "age":23,
#         "country":"IND"
#     },
#     2:{
#         "name": "Ankit",
#         "age": 22,
#         "country": "USA"
#     },
#     3:{
#         "name": "Adarsh",
#         "age": 21,
#         "country": "AUS"
#     }
# }

# class Student(BaseModel):
#     name:str
#     age:int
#     country:str

# class UpdateStudent(BaseModel):
#     name:Optional[str]=None
#     age:Optional[int]=None
#     country:Optional[str]=None

# @app.get("/",tags=['Home']) #called path in FastAPI [@app=decorator,get=operation ,/=path===>path operation decorator]
# async def root():
#     return {"data":"Aman Kumar!"}

# @app.get("/get-data",tags=['GET'])
# async def get_stu_data():
#     return students

# @app.get("/get-student-data/{student_id}",tags=['GET'])
# async def get_stu_data_id(*,student_id:int,name:Optional[str]=None,age:int):
#     for k,v in students.items():
#         if k == student_id and v["age"] == age:
#             return v
#     return {"Data": "Not found"}
    

# @app.get("/get-student-data-check/{student_id}",tags=['GET'])
# async def get_data_check(student_id:int,age:int):
#     for k,v in students.items():
#         if k ==student_id and v['age']==age:
#             return {"data":v}         
#     return {"Data": "Not found"}


#Blog is a model created to get the data from user and pass it to API for further execution
class Blog(BaseModel):
    title:str
    body:str
    published:Optional[bool]



#fastAPI reads data line-by-line
#pydantic is used for data validation--->supports str,int,bool,float
#using localhost:8000/docs---> we can see documentation using swagger UI,or we can use redoc
@app.get('/',tags=['Home'])
async def index():
    return {'data':'bloglist'}

#query parameter:--> localhost:8000/blog?limit=12&published=false
@app.get('/blog',tags=['Get'])
#async def display(limit=10,published:bool=True,sort:Optional[str]=None):
async def display(limit:int,published:bool,sort:Optional[str]=None):
    if published:
        return {'data':f'{limit} published blogs from db'}
    else:
        return {'data':f'{limit} blogs from db'}

@app.get('/blog/unpublished',tags=['Get'])
async def show():
    #fetch blog with id=id
    return {'data':"all unpublished blogs"}

@app.get('/blog/{id}',tags=['Get'])
async def show(id:int):
    #fetch blog with id=id
    return {'data':id}

@app.get('/blog/{id}/comment',tags=['Get'])
async def comment(id:int):
    #fetch comment with id=id
    return {'data':{'1','2'}}


#request body in post method
@app.post('/blog',tags=['Post'])
async def create_blog(blog:Blog):
    data=f"Blog is created with title as {blog.title}"
    #breakpoint()
    #----->apply the breakpoint and hit the endpoint in postman to enable pdb
    #commnand inside pdb:p,n,"q to quit"
    return {"data":data}




##for debugging purpose we create this
### after creating these two lines we can directly run command:-->python main.py

# if __name__ == "__main__":
#     uvicorn.run(app,host='127.0.0.1',port=8000)