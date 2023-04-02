from sqlalchemy.orm import Session
# from schemas import schema
# from models import model

from fastapi_mail import FastMail, MessageSchema, ConnectionConfig
from fastapi.templating import Jinja2Templates
import tracemalloc
tracemalloc.start()
templates = Jinja2Templates(directory="email")

conf = ConnectionConfig(
    MAIL_USERNAME="email",
    MAIL_PASSWORD="password",
    MAIL_FROM="email@gmail.com",
    MAIL_PORT=587,
    MAIL_SERVER="email",
    MAIL_TLS=True,
    MAIL_SSL=False,
    USE_CREDENTIALS=False,
    VALIDATE_CERTS=True
)

async def create_mail(customer_id: int):
    try:
        message = MessageSchema(
        subject="CoffeCrazy survey",
        recipients=["recipient"],
        body="asdasd"
    )
    except:
        message = MessageSchema(
        subject="CoffeCrazy survey",
        recipients=["recipient"],
        body="asdasd"
    )
    fm = FastMail(conf)
    await fm.send_message(message)
    return 1