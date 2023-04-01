from schemas import schema
from models import model
from database import SessionLocal, engine
from utils import token_crud, qr_code
import os

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