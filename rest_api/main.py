from fastapi import Depends, FastAPI
from routers import token, coupon, quest, battlepass, customer, monster, leaderboard, spinningwheel, survey
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
        "customer_id": 14
    })
)
app.include_router(token.router)
app.include_router(customer.router)
app.include_router(spinningwheel.router)
app.include_router(survey.router)
if int(tier_picked.text) <= 1 and int(tier_picked.text) != 0:
    app.include_router(quest.router)
    app.include_router(coupon.router)
    app.include_router(spinningwheel.router)
elif int(tier_picked.text) <= 2 and int(tier_picked.text) !=0:
    app.include_router(quest.router)
    app.include_router(coupon.router)
    app.include_router(leaderboard.router)
    app.include_router(spinningwheel.router)
elif int(tier_picked.text) <= 3 and int(tier_picked.text) !=0:
    app.include_router(quest.router)
    app.include_router(coupon.router)
    app.include_router(leaderboard.router)
    app.include_router(battlepass.router)
    app.include_router(monster.router)


