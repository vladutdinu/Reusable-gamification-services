from fastapi import Depends, FastAPI
from routers import token, coupon, quest, battlepass, customer, monster, leaderboard, spinningwheel
import models, schemas
from utils import token_crud
from database import SessionLocal, engine
from fastapi.middleware.cors import CORSMiddleware
import requests
import json

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

api_token = token_crud.get_token(1, SessionLocal())
tier_picked = requests.post("http://localhost:8005/customer/validate_token/",
    data=json.dumps({
        "token": api_token.__dict__['token'],
        "customer_id": 1
    })
)
app.include_router(token.router)
app.include_router(customer.router)


if 3<= 1 and 3!= 0:
    app.include_router(quest.router)
    app.include_router(coupon.router)
   # app.include_router(spinningwheel.router)
elif 3<= 2 and 3!=0:
    app.include_router(quest.router)
    app.include_router(coupon.router)
    app.include_router(leaderboard.router)
    app.include_router(spinningwheel.router)
elif 3<= 3 and 3!=0:
    app.include_router(quest.router)
    app.include_router(coupon.router)
    app.include_router(leaderboard.router)
    app.include_router(battlepass.router)
    app.include_router(monster.router)


