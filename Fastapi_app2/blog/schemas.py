from typing import List 
from pydantic import BaseModel

class Blog(BaseModel):
    body:str
    title:str
    
    class Config:
        orm_mode=True
       
#class ShowBlog(Blog):---> you can use either Blog or BaseModel to extend the property
    
class User(BaseModel):
    name:str
    email:str
    password:str
    
    class Config:
        orm_mode=True
 
class ShowUser(BaseModel):
    name:str
    email:str
    blogs:List[Blog]=True
    class Config:
        orm_mode=True 
    
class ShowBlog(BaseModel):
    title:str
    body:str
    creator:ShowUser
    
    class Config:
        orm_mode=True
    
   
    