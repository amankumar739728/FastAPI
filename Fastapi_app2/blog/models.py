from sqlalchemy import Column,Integer,String,ForeignKey
from database import Base
from sqlalchemy.orm import relationship 



class Blog(Base):
    __tablename__ ='blogs'
    
    id=Column(Integer,primary_key=True,index=True)
    title=Column(String)
    body=Column(String)
    #users is tablename and id is col
    user_id =Column(Integer,ForeignKey('users.id'))  
    
    #Relationship between user and blog
    creator=relationship("User",back_populates="blogs")
    

    
    
#create a table named 'user' to store the record in database.
class User(Base):
    __tablename__ ='users'
    
    id=Column(Integer,primary_key=True,index=True)
    name=Column(String)
    email=Column(String)
    password=Column(String)
    
    #relationship
    blogs = relationship('Blog',back_populates="creator")