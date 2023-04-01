import json
from sqlalchemy.orm import Session
from schemas import schema
from models import model

def create_product(product: model.Product, db: Session):
    new_tier = schema.Product(
       
       name=product.name,
       description=product.description,
       price=product.price,
       type=product.type

    )
    db.add(new_tier)
    db.commit()
    db.refresh(new_tier)
    return new_tier
def get_product_by_id(product_id: int, db: Session):
    product = db.query(schema.Product).filter(schema.Product.id == product_id).first()
    return product
def get_product_by_name(product_name: str, db: Session):
    product = db.query(schema.Product).filter(schema.Product.name == product_name).first()
    return product

def update_product(product: model.Product, db: Session):
    result = db.query(schema.Product).filter(schema.Product.id == product.id).update(
        {
            "name":product.name,
            "description":product.description,
            "price":product.price,
            "type":product.type
        }
    )
    db.commit()
    return result
def delete_product(product_id: int, db: Session):
    result = db.query(schema.Product).filter(schema.Product.id == product_id).delete()
    db.commit()
    return result
def get_all_products( db: Session):
    product = db.query(schema.Product).all()
    return product