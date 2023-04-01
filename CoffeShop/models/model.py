from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel, EmailStr
from typing import Optional, List



app = FastAPI()

class Type(BaseModel):
    id:int
    typeOf:str
    
class Product(BaseModel):
    id:int
    name:str
    description:str
    price:int
    type:Type
class User(BaseModel):
    id:int
    name:str
    email:str
    password:str
    ranking:int
class UserSignUp(BaseModel):
  
    name:str
    email:str
    password:str
    password2:str
class UserLogIn(BaseModel):
    password:str
    email:str  


