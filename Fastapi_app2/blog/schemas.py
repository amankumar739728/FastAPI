from typing import List,Optional
from pydantic import BaseModel

class BlogBase(BaseModel):
    title:str
    body:str

class Blog(BlogBase):
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
    blogs:List[Blog]=[]
    class Config:
        orm_mode=True 
    
class ShowBlog(BaseModel):
    title:str
    body:str
    creator:Optional[ShowUser] = None
    
    class Config:
        orm_mode=True
    
   
class Login(BaseModel):
    username:str
    password:str 
    
    
class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: Optional[str] = None   