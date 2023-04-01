from typing import List
from fastapi import APIRouter, Depends, HTTPException, Response
from utils import product_crud
from models import model
from database import SessionLocal
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

router = APIRouter(prefix="/product", tags=["Customer Endpoints"])
@router.post("/")
async def create_item(product: model.Product, db: get_db = Depends()):
    result = product_crud.get_product(product.id, db)
    if result:
        raise HTTPException(status_code=400, detail="Product already exists")
    return product_crud.create_customer(product, db)
@router.get("/{product_id}", response_model=model.Product)
async def get_product_by_id(product_id: int, db: get_db = Depends()):
    result = product_crud.get_product_by_id(product_id, db)
    if result:
        return result
    else:
        raise HTTPException(status_code=400, detail="Product doesnt exist")
@router.get("/{product_name}", response_model=model.Product)
async def get_product_by_name(product_name: str, db: get_db = Depends()):
    result = product_crud.get_product_by_name(product_name, db)
    if result:
        return result
    else:
        raise HTTPException(status_code=400, detail="Product doesnt exist")
@router.put("/", response_model=model.Product)
async def update_product(product: model.Product, db: get_db = Depends()):
    result = product_crud.update_product(product, db)
    if result:
        return product_crud.get_product_by_id(product.id, db)
    else:
        raise HTTPException(status_code=400, detail="Product doesnt exist")

@router.delete("/{product_id}", response_model=model.Product)
async def delete_product(product_id: int, db: get_db = Depends()):
    result = product_crud.delete_product(product_id, db)
    if result:
        return Response("Product deleted")
    else:
        raise HTTPException(status_code=400, detail="Product doesnt exist")