from fastapi import Depends, FastAPI
from routers import user, product, type
import models, schemas
from database import SessionLocal, engine

app = FastAPI()

app.include_router(user.router)
app.include_router(product.router)
app.include_router(type.router)