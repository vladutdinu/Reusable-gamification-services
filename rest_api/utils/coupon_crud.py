from sqlalchemy.orm import Session
from schemas import schema
from models import model

def create_coupon(coupon: model.Coupon, db: Session):
    new_coupon = schema.Coupon(
        customer_id = coupon.customer_id,
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
    coupon = db.query(schema.Coupon).filter(schema.Coupon.id == coupon_id).first()
    return coupon

def get_coupons_customer(customer_id: int, db: Session):
    coupon = db.query(schema.Coupon).filter(schema.Coupon.customer_id == customer_id).all()
    return coupon
    
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

def update_coupon_status(coupon: model.Coupon, status: int, db: Session):
    result = db.query(schema.Coupon).filter(schema.Coupon.id == coupon.id).update(
        {
           "done": status
        }
    )
    db.commit()
    return result

def delete_coupon(coupon_id: int, db: Session):
    result = db.query(schema.Coupon).filter(schema.Coupon.id == coupon_id).delete()
    db.commit()
    return result