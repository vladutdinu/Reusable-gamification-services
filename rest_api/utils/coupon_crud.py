from sqlalchemy.orm import Session
from schemas import schema
from models import model

def create_coupon(coupon: model.Coupon, db: Session):
    new_coupon = schema.Coupon(
        description = coupon.description,
        discount = coupon.discount,
        code = coupon.code,
        start_date = coupon.start_date,
        end_date = coupon.end_date
    )
    db.add(new_coupon)
    db.commit()
    db.refresh(new_coupon)
    return new_coupon

def get_coupon(coupon_id: int, db: Session):
    token = db.query(schema.Coupon).filter(schema.Coupon.id == coupon_id).first()
    return token
    
def update_coupon(coupon: model.Coupon, db: Session):
    result = db.query(schema.Coupon).filter(schema.Coupon.id == coupon.id).update(
        {
           "description": coupon.description,
           "discount": coupon.discount,
           "code": coupon.code,
           "start_date": coupon.start_date,
           "end_date": coupon.end_date
        }
    )
    db.commit()
    return result

def delete_coupon(coupon_id: int, db: Session):
    result = db.query(schema.Coupon).filter(schema.Coupon.id == coupon_id).delete()
    db.commit()
    return result

