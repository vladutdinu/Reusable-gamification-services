from schemas import schema
from models import model
from database import SessionLocal, engine
from utils import token_crud, qr_code, monster_crud, coupon_crud, spinningwheel_crud, leaderboard_crud, battlepass_crud
import os
import base64
schema.Base.metadata.create_all(bind=engine)

TOKEN = "token" #os.environ["TOKEN"]

tokens = [
    {
        "qr_code": qr_code.generate_qr_code("http://localhost:8002/qr_code?id="),
        "token": TOKEN
    }
]

for token in tokens:
    token_crud.create_token(model.Token(
        qr_code = token['qr_code'],
        token = token['token']
    ).copy(),  SessionLocal())

for monster_path in os.listdir("./monstruleti"):
    monster_crud.create_monster(model.Monster(
        name=monster_path
    ).copy(), SessionLocal())

coupons = [
    {
        "customer_id": 1,
        "description": "Get discount on your next coffe",
        "discount": 10,
        "code": "CODE1",
        "start_date": "2023-04-01",
        "end_date": "2023-04-05",
    },
    {
        "customer_id": 1,
        "description": "Get discount on your next sandwich",
        "discount": 10,
        "code": "CODE2",
        "start_date": "2023-04-01",
        "end_date": "2023-04-05",
    },
    {
        "customer_id": 2,
        "description": "Get discount on your next drink",
        "discount": 10,
        "code": "CODE3",
        "start_date": "2023-04-01",
        "end_date": "2023-04-05",
    },
    {
        "customer_id": 2,
        "description": "Get discount on your next sandwich",
        "discount": 10,
        "code": "CODE4",
        "start_date": "2023-04-01",
        "end_date": "2023-04-05",
    }
]

for coupon in coupons:
    coupon_crud.create_coupon(
        model.Coupon(
            customer_id = coupon['customer_id'],
            description = coupon['description'],
            discount = coupon['discount'],
            code = coupon['code'],
            start_date = coupon['start_date'],
            end_date = coupon['end_date'],
        ), SessionLocal()
    )

quests = [
    {
        "customer_id": 1,
        "quest": "string",
  "target_quantity": 0,
  "type": "string",
  "quantity": 0,
  "product_id": 0,
  "points": 0,
        "start_date": "2023-04-01",
        "end_date": "2023-04-05",
    },
    {
        "customer_id": 1,
        "quest": "string",
  "target_quantity": 0,
  "type": "string",
  "quantity": 0,
  "product_id": 0,
  "points": 0,
        "start_date": "2023-04-01",
        "end_date": "2023-04-05",
    },
    {
        "customer_id": 2,
        "quest": "string",
  "target_quantity": 0,
  "type": "string",
  "quantity": 0,
  "product_id": 0,
  "points": 0,
        "start_date": "2023-04-01",
        "end_date": "2023-04-05",
    },
    {
        "customer_id": 2,
        "quest": "string",
  "target_quantity": 0,
  "type": "string",
  "quantity": 0,
  "product_id": 0,
  "points": 0,
        "start_date": "2023-04-01",
        "end_date": "2023-04-05",
    }
]

for coupon in coupons:
    coupon_crud.create_coupon(
        model.Coupon(
            customer_id = coupon['customer_id'],
            description = coupon['description'],
            discount = coupon['discount'],
            code = coupon['code'],
            start_date = coupon['start_date'],
            end_date = coupon['end_date'],
        ), SessionLocal()
    )