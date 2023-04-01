from fastapi import Depends, FastAPI
from routers import token, coupon, quest, battlepass, customer, monster, leaderboard
import models, schemas
from database import SessionLocal, engine
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(token.router)
app.include_router(coupon.router)
app.include_router(quest.router)
app.include_router(battlepass.router)
app.include_router(customer.router)
app.include_router(monster.router)
app.include_router(leaderboard.router)
