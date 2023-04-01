from schemas import schema
from models import model
from database import SessionLocal, engine
from utils import token_crud, qr_code, monster_crud
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