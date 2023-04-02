from schemas import schema
from models import model
from database import SessionLocal, engine
from utils import token_crud, qr_code, monster_crud, leaderboard_crud, customer_crud, quest_crud, coupon_crud, spinningwheel_crud, leaderboard_crud, battlepass_crud
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

customers=[
    {
        "customer_id": 1
    },
    {
        "customer_id": 2
    }
]

for customer in customers:
    customer_crud.create_customer(
        model.Customer(
            customer_id=customer['customer_id']
        ), SessionLocal()
    )

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
        "quest": "Buy 1 coffe",
        "target_quantity": 1,
        "type": "Daily",
        "quantity": 0,
        "product_id": 1,
        "points": 100,
        "start_date": "2023-04-01",
        "end_date": "2023-04-05",
    },
    {
        "customer_id": 1,
        "quest": "Buy 2 drinks",
        "target_quantity": 2,
        "type": "Weekly",
        "quantity": 0,
        "product_id": 7,
        "points": 100,
        "start_date": "2023-04-01",
        "end_date": "2023-04-05",
    },
    {
        "customer_id": 1,
        "quest": "Buy 4 sandwiches",
        "target_quantity": 4,
        "type": "Montly",
        "quantity": 0,
        "product_id": 4,
        "points": 100,
        "start_date": "2023-04-01",
        "end_date": "2023-04-05",
    },
    {
        "customer_id": 2,
        "quest": "Buy 1 coffe",
        "target_quantity": 1,
        "type": "Daily",
        "quantity": 0,
        "product_id": 1,
        "points": 100,
        "start_date": "2023-04-01",
        "end_date": "2023-04-05",
    },
    {
        "customer_id": 2,
        "quest": "Buy 2 drinks",
        "target_quantity": 2,
        "type": "Weekly",
        "quantity": 0,
        "product_id": 7,
        "points": 100,
        "start_date": "2023-04-01",
        "end_date": "2023-04-05",
    },
     {
        "customer_id": 2,
        "quest": "Buy 4 sandwiches",
        "target_quantity": 4,
        "type": "Montly",
        "quantity": 0,
        "product_id": 4,
        "points": 100,
        "start_date": "2023-04-01",
        "end_date": "2023-04-05",
    },
]

for quest in quests:
    quest_crud.create_quest(
        model.Quest(
            customer_id = quest['customer_id'],
            quest = quest['quest'],
            target_quantity = quest['target_quantity'],
            type = quest['type'],
            quantity = quest['quantity'],
            product_id = quest['product_id'],
            points = quest['points'],
            start_date = quest['start_date'],
            end_date = quest['end_date'],
        ), SessionLocal()
    )

battlepass_crud.create_battlepass(model.Battlepass(
    customer_id = 1,
    start_date = "2023-04-01",
    end_date = "2023-04-05",
), SessionLocal())

battlepass_crud.create_battlepass(model.Battlepass(
    customer_id = 2,
    start_date = "2023-04-01",
    end_date = "2023-04-05",
), SessionLocal())

targets = [
    {
        "product_id": 1,
        "target_points": 100,
        "battlepass_id": 1,
    },
    {
        "product_id": 4,
        "target_points": 200,
        "battlepass_id": 1,
    },
    {
        "product_id": 7,
        "target_points": 300,
        "battlepass_id": 1,
    },
    {
        "product_id": 2,
        "target_points": 100,
        "battlepass_id": 2,
    },
    {
        "product_id": 5,
        "target_points": 100,
        "battlepass_id": 2,
    },
    {
        "product_id": 8,
        "target_points": 100,
        "battlepass_id": 2,
    }
]

for target in targets:
    battlepass_crud.create_target(model.Target(
        product_id=target['product_id'],
        target_points=target['target_points'],
        battlepass_id=target['battlepass_id']
    ), SessionLocal())

leaderboard_crud.create_leaderboard(model.Leaderboard(
    start_date = "2023-04-01",
    end_date = "2023-04-05",
), SessionLocal())

spinningwheel_crud.create_spinning_wheel(model.SpinningWheel(
    start_date = "2023-04-01",
    end_date = "2023-04-05",
), SessionLocal())

sw_rewards = [
    {
        "product_id": 1,
        "spinning_wheel_id": 1
    },
    {
        "product_id": 2,
        "spinning_wheel_id": 1
    },
    {
        "product_id": 3,
        "spinning_wheel_id": 1
    },
    {
        "product_id": 4,
        "spinning_wheel_id": 1
    },
    {
        "product_id": 5,
        "spinning_wheel_id": 1
    },
    {
        "product_id": 6,
        "spinning_wheel_id": 1
    },
]

for sw_reward in sw_rewards:
    spinningwheel_crud.create_spinning_wheel_reward(model.SpinningWheelReward(
        product_id = sw_reward['product_id'],
        spinning_wheel_id = sw_reward['spinning_wheel_id']
    ), SessionLocal())