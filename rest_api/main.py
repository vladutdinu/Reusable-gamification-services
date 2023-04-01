from fastapi import Depends, FastAPI
from routers import token, coupon, quest, battlepass
import models, schemas
from database import SessionLocal, engine

app = FastAPI()

app.include_router(token.router)
app.include_router(coupon.router)
app.include_router(quest.router)
app.include_router(battlepass.router)
