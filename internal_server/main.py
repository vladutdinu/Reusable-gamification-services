from fastapi import Depends, FastAPI
from routers import customer, gamification, tier
import models, schemas
from database import SessionLocal, engine

app = FastAPI()

app.include_router(customer.router)
app.include_router(gamification.router)
app.include_router(tier.router)