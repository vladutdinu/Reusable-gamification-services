from typing import List
from fastapi import APIRouter, Depends, HTTPException, Response
from utils import coupon_crud
from models import model
from database import SessionLocal

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

router = APIRouter(prefix="/coupon", tags=["Coupon Endpoints"])

@router.post("/", response_model=model.Coupon)
async def create_coupon(coupon: model.Coupon, db: get_db = Depends()):
    result = coupon_crud.get_coupon(coupon.id, db)
    if result:
        raise HTTPException(status_code=400, detail="Coupon already exist")
    return coupon_crud.create_coupon(coupon, db).__dict__

@router.get("/{coupon_id}", response_model=model.Coupon)
async def get_coupon(coupon_id: int, db: get_db = Depends()):
    result = coupon_crud.get_coupon(coupon_id, db)
    if result:
        return result.__dict__
    else:
        raise HTTPException(status_code=400, detail="Coupon doesnt exist")
    
@router.get("/all/{customer_id}", response_model=List[model.Coupon])
async def get_coupons_customer(customer_id: int, db: get_db = Depends()):
    result = coupon_crud.get_coupons_customer(customer_id, db)
    if result:
        return [coupon.__dict__ for coupon in result]
    else:
        raise HTTPException(status_code=400, detail="No coupons")

@router.put("/", response_model=model.Coupon)
async def update_coupon(coupon: model.Coupon, db: get_db = Depends()):
    result = coupon_crud.update_coupon(coupon, db)
    if result:
        return coupon_crud.get_coupon(coupon.id, db).__dict__
    else:
        raise HTTPException(status_code=400, detail="Coupon doesnt exist")

@router.put("/use/")
async def use_coupon(coupon_id: int, customer_id, db: get_db = Depends()):
    return coupon_crud.use_coupon(coupon_id, customer_id, db)

@router.put("/activate/")
async def activate_coupon(coupon_id: int, customer_id, db: get_db = Depends()):
    return coupon_crud.activate_coupon(coupon_id, customer_id, db)

@router.put("/", response_model=model.Coupon)
async def update_coupon_status(coupon_id: int, status: int, db: get_db = Depends()):
    result = coupon_crud.update_coupon_status(coupon_id, status, db)
    if result:
        return coupon_crud.get_coupon(coupon_id, db).__dict__
    else:
        raise HTTPException(status_code=400, detail="Coupon doesnt exist")

@router.delete("/{coupon_id}", response_model=model.Coupon)
async def delete_coupon(coupon_id: int, db: get_db = Depends()):
    result = coupon_crud.delete_coupon(coupon_id, db)
    if result:
        return Response("Coupon deleted")
    else:
        raise HTTPException(status_code=400, detail="Coupon doesnt exist")