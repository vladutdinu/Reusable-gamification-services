from schemas import schema
from models import model
from database import SessionLocal, engine
from utils import product_crud, type_crud, user_crud

schema.Base.metadata.create_all(bind=engine)

types = [
    {
        "typeOf": "Coffe"
    },
    {
        "typeOf": "Sandwiches"
    },
    {
        "typeOf": "Drinks"
    }
]

for type in types:
    type_crud.create_type(
        model.Type(
            typeOf=type['typeOf']
        ), SessionLocal()
    )

products=[
    {
        "name": "Coffe1",
        "description": "Coffe1",
        "price": 10,
        "type": 1
    },
    {
        "name": "Coffe1",
        "description": "Coffe1",
        "price": 11,
        "type": 1
    },
    {
        "name": "Coffe2",
        "description": "Coffe1",
        "price": 12,
        "type": 1
    },
    {
        "name": "Sandwich1",
        "description": "Sandwich1",
        "price": 10,
        "type": 2
    },
    {
        "name": "Sandwich2",
        "description": "Sandwich2",
        "price": 11,
        "type": 2
    },
    {
        "name": "Sandwich3",
        "description": "Sandwich3",
        "price": 12,
        "type": 2
    },
    {
        "name": "Drink1",
        "description": "Drink1",
        "price": 10,
        "type": 3
    },
    {
        "name": "Drink2",
        "description": "Drink2",
        "price": 11,
        "type": 3
    },
    {
        "name": "Drink3",
        "description": "Drink3",
        "price": 12,
        "type": 3
    },
]

for product in products:
    product_crud.create_product(
        model.Product(
            name=product['name'],
            description=product['description'],
            price=product['price'],
            type=product['type']
        ), SessionLocal()
    )

users=[
    {
        "name": "u1",
        "email": "user1@gmail.com",
        "password": "pass1"
    },
    {
        "name": "u2",
        "email": "user2@gmail.com",
        "password": "pass2"
    }
]

for user in users:
    user_crud.create_user(
        model.User(
            name=user['name'],
            email=user['email'],
            password=user['password']
        ), SessionLocal()
    )