from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel, EmailStr
from typing import Optional, List

app = FastAPI()

class Type(BaseModel):
    id: Optional[int]
    typeOf: str


class Product(BaseModel):
    id: Optional[int]
    name: str
    description: str
    price: int
    type: int


class User(BaseModel):
    id: Optional[int]
    name: str
    email: str
    password: str
    


class UserSignUp(BaseModel):

    name: str
    email: str
    password: str
    password2: str


class UserLogIn(BaseModel):
    password: str
    email: str


class UserChangePassword(BaseModel):
    id: int
    password1: str
    password2: str
