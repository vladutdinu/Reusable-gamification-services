from sqlalchemy.orm import Session
from schemas import schema
from models import model
from utils import customer_crud

def create_coupon(coupon: model.Coupon, db: Session):
    new_coupon = schema.Coupon(
        customer_id = coupon.customer_id,
        product_id = coupon.product_id,
        description = coupon.description,
        discount = coupon.discount,
        points_required = coupon.points_required,
        code = coupon.code,
        start_date = coupon.start_date,
        end_date = coupon.end_date,
        active = 0
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
           "points_required": coupon.points_required,
           "code": coupon.code,
           "start_date": coupon.start_date,
           "end_date": coupon.end_date
        }
    )
    db.commit()
    return result

def activate_coupon(coupon_id: int, customer_id, db: Session):
    coupon = get_coupon(coupon_id, db)
    customer = customer_crud.get_customer_with_points_by_id(customer_id, db)
    if coupon.points_required <= customer.points.current_points and coupon.done == 0:
        coupon.active = 1
        update_coupon(coupon, db)
        return 1
    else:
        return 0 

def use_coupon(coupon_id: int, customer_id, db: Session):
    coupon = get_coupon(coupon_id, db)
    customer = customer_crud.get_customer_with_points_by_id(customer_id, db)
    if coupon.points_required <= customer.points.current_points and coupon.done == 0:
        coupon.active = 1
        update_coupon_status(coupon, 1, db)
        customer.points.current_points -= coupon.points_required
        customer_crud.update_customer_points(customer.points, db)
        return 1
    else:
        return 0 
    
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