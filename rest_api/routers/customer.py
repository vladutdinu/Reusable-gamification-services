from fastapi import APIRouter, Depends, HTTPException, Response
from utils import customer_crud
from models import model
from database import SessionLocal

# Dependency

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

router = APIRouter(prefix="/customer", tags=["Customer Endpoints"])

@router.post("/", response_model=model.Customer)
async def create_customer(customer: model.Customer, db: get_db = Depends()):
    result = customer_crud.get_customer_by_id(customer.id, db)
    if result:
        raise HTTPException(status_code=400, detail="Customer already exist")
    return customer_crud.create_customer(customer, db).__dict__

@router.get("/{customer_id}", response_model=model.CustomerWithPoints)
async def get_customer_by_id(customer_id: int, db: get_db = Depends()):
    result = customer_crud.get_customer_with_points_by_id(customer_id, db)
    if result:
        return result.__dict__
    else:
        raise HTTPException(status_code=400, detail="Customer doesnt exist")

@router.put("/", response_model=model.Customer)
async def update_customer(customer: model.Customer, db: get_db = Depends()):
    result = customer_crud.update_customer(customer, db)
    if result:
        return customer_crud.get_customer_by_id(customer.id, db).__dict__
    else:
        raise HTTPException(status_code=400, detail="Customer doesnt exist")

@router.delete("/{customer_id}", response_model=model.Customer)
async def delete_customer(customer_id: int, db: get_db = Depends()):
    result = customer_crud.delete_customer(customer_id, db)
    if result:
        return Response("Customer deleted")
    else:
        raise HTTPException(status_code=400, detail="Customer doesnt exist")

@router.post("/points/", response_model=model.CustomerPoints)
async def create_target(target: model.CustomerPoints, db: get_db = Depends()):
    result = customer_crud.get_customer_points(target.id, db)
    if result:
        raise HTTPException(status_code=400, detail="CustomerPoints already exist")
    return customer_crud.create_customer_points(target, db).__dict__


@router.get("/points/{customer_points_id}", response_model=model.CustomerPoints)
async def get_target(customer_points_id: int, db: get_db = Depends()):
    result = customer_crud.get_customer_points(customer_points_id, db)
    if result:
        return result.__dict__
    else:
        raise HTTPException(status_code=400, detail="CustomerPoints doesnt exist")


@router.put("/points/", response_model=model.CustomerPoints)
async def update_target(customer_point: model.CustomerPoints, db: get_db = Depends()):
    result = customer_crud.update_customer_points(customer_point, db)
    if result:
        return customer_crud.get_customer_points(customer_point.id, db).__dict__
    else:
        raise HTTPException(status_code=400, detail="CustomerPoints doesnt exist")


@router.delete("/points/{customer_points_id}", response_model=model.CustomerPoints)
async def delete_target(customer_points_id: int, db: get_db = Depends()):
    result = customer_crud.delete_customer_points(customer_points_id, db)
    if result:
        return Response("CustomerPoints deleted")
    else:
        raise HTTPException(status_code=400, detail="CustomerPoints doesnt exist")

