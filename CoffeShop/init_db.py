from schemas import schema
from models import model
from database import SessionLocal, engine


schema.Base.metadata.create_all(bind=engine)

