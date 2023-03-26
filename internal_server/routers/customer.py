from typing import List
from fastapi import APIRouter, Depends, HTTPException, Response
from utils import customer_crud
from models import model
from schemas import schema
from database import SessionLocal

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

router = APIRouter(prefix="/customer", tags=["Customer Endpoints"])

@router.post("/")
async def create_item(customer: model.Customer, db: get_db = Depends()):
    result = customer_crud.get_customer(customer.id, db)
    if result:
        raise HTTPException(status_code=400, detail="Customer already exists")
    return customer_crud.create_customer(customer, db)

@router.get("/{customer_id}", response_model=model.Customer)
async def get_customer(customer_id: int, db: get_db = Depends()):
    result = customer_crud.get_customer(customer_id, db)
    if result:
        return result
    else:
        raise HTTPException(status_code=400, detail="Customer doesnt exist")

@router.get("/customer/{customer_name}", response_model=model.Customer)
async def get_customer(customer_name: str, db: get_db = Depends()):
    result = customer_crud.get_customer(customer_name, db)
    if result:
        return result
    else:
        raise HTTPException(status_code=400, detail="Customer doesnt exist")

@router.get("/tiers/")
async def get_customers_tiers_type(db: get_db = Depends()):
    return customer_crud.get_customers_tiers_type(db)

@router.put("/", response_model=model.Customer)
async def update_customer(customer: model.Customer, db: get_db = Depends()):
    result = customer_crud.update_customer(customer, db)
    if result:
        return customer_crud.get_customer(customer.id, db)
    else:
        raise HTTPException(status_code=400, detail="Tier doesnt exist")

@router.delete("/{customer_id}", response_model=model.Customer)
async def delete_customer(customer_id: int, db: get_db = Depends()):
    result = customer_crud.delete_customer(customer_id, db)
    if result:
        return Response("Customer deleted")
    else:
        raise HTTPException(status_code=400, detail="Customer doesnt exist")