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

@router.put("/", response_model=model.Coupon)
async def update_coupon(coupon: model.Coupon, db: get_db = Depends()):
    result = coupon_crud.update_coupon(coupon, db)
    if result:
        return coupon_crud.get_coupon(coupon.id, db).__dict__
    else:
        raise HTTPException(status_code=400, detail="Coupon doesnt exist")

@router.delete("/{coupon_id}", response_model=model.Coupon)
async def delete_coupon(coupon_id: int, db: get_db = Depends()):
    result = coupon_crud.delete_coupon(coupon_id, db)
    if result:
        return Response("Coupon deleted")
    else:
        raise HTTPException(status_code=400, detail="Coupon doesnt exist")