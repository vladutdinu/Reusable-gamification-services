from typing import List
from fastapi import APIRouter, Depends, HTTPException, Response
from utils import type_crud
from models import model
from database import SessionLocal
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

router = APIRouter(prefix="/type", tags=["Type Endpoints"])
@router.post("/")
async def create_item(type: model.Type, db: get_db = Depends()):
    result = type_crud.get_product(type.id, db)
    if result:
        raise HTTPException(status_code=400, detail="Type already exists")
    return type_crud.create_customer(type, db)
@router.get("/{type_name}", response_model=model.Type)
async def get_type_by_name(type_name: str, db: get_db = Depends()):
    result = type_crud.get_type_by_name(type_name, db)
    if result:
        return result
    else:
        raise HTTPException(status_code=400, detail="Type doesnt exist")
@router.put("/", response_model=model.Type)
async def update_product(type: model.Type, db: get_db = Depends()):
    result = type_crud.update_product(type, db)
    if result:
        return type_crud.get_product_by_id(type.id, db)
    else:
        raise HTTPException(status_code=400, detail="Product doesnt exist")

@router.delete("/{product_id}", response_model=model.Customer)
async def delete_customer(type_id: int, db: get_db = Depends()):
    result = type_crud.delete_product(type_id, db)
    if result:
        return Response("type deleted")
    else:
        raise HTTPException(status_code=400, detail="type doesnt exist")