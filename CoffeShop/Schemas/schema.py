from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from database import Base

class Type(Base):
    __tablename__ = "types"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    typeOf=Column(String)
class Product(Base):
    __tablename__ = "products"
    id=Column(Integer, primary_key=True, index=True, autoincrement=True)
    name=Column(String)
    description=Column(String)
    price=Column(Integer)
    type=Column(Integer, ForeignKey("types.id"))
class User(Base):
    __tablename__ = "users"
    id=Column(Integer, primary_key=True, index=True, autoincrement=True)
    name=Column(String)
    email=Column(String)
    password=Column(String)
    ranking=Column(Integer)

