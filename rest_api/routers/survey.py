from fastapi import APIRouter, Depends, HTTPException, Response
from utils import surver_crud
from models import model
from database import SessionLocal

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

router = APIRouter(prefix="/survey", tags=["Survey Endpoints"])

@router.post("/{customer_id}")
async def create_email(customer_id: int, db: get_db = Depends()):
    result = surver_crud.create_email(customer_id, db)
    return result