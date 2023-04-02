from fastapi import Depends, FastAPI
from routers import user, product, type
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
app.include_router(user.router)
app.include_router(product.router)
app.include_router(type.router)