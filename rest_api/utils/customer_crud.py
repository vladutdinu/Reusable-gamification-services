from sqlalchemy.orm import Session
from schemas import schema
from models import model

def create_customer(customer: model.Customer, db: Session):
    customer_points = create_customer_points(model.CustomerPoints(points = 0), db)
    new_customer = schema.Customer(
        customer_id=customer.customer_id,
        points_id=customer_points.id
    )
    db.add(new_customer)
    db.commit()
    db.refresh(new_customer)
    return new_customer

def get_customer_by_id(customer_id: int, db: Session):
    targets = db.query(schema.Customer).filter(
        schema.Target.id == customer_id).first()
    return targets

def get_customer_with_points_by_id(customer_id: int, db: Session):
    customer = db.query(schema.Customer).filter(
        schema.Customer.id == customer_id).first()
    customer_points = db.query(schema.CustomerPoints).filter(schema.CustomerPoints.id == customer.points_id).first()
    return model.CustomerWithPoints(
       id = customer.id,
       customer_id = customer.customer_id,
       points = customer_points.__dict__
    )

def get_customer(battlepass_id: int, db: Session):
    targets = db.query(schema.Customer).filter(
        schema.Target.battlepass_id == battlepass_id).all()
    return targets

def update_customer(customer: model.Customer, db: Session):
    result = db.query(schema.Customer).filter(schema.Customer.id == customer.id).update(
        {
            "customer_id": customer.customer_id,
            "points_id": customer.points_id
        }
    )
    db.commit()
    return result

def delete_customer(customer_id: int, db: Session):
    customer = db.query(schema.Customer).filter(
        schema.Customer.id == customer_id).delete()
    customer_points = delete_customer_points(customer_id, db)
    db.commit()
    if customer and customer_points:
        return 1
    else:
        return 0

def create_customer_points(points: model.CustomerPoints, db: Session):
    new_customers_points = schema.CustomerPoints(
        points=points.points
    )
    db.add(new_customers_points)
    db.commit()
    db.refresh(new_customers_points)
    return new_customers_points


def get_customer_points(customer_points_id: int, db: Session):
    token = db.query(schema.CustomerPoints).filter(
        schema.CustomerPoints.id == customer_points_id).first()
    return token

def update_customer_points(customer_points: model.CustomerPoints, db: Session):
    result = db.query(schema.CustomerPoints).filter(schema.CustomerPoints.id == customer_points.id).update(
        {
            "points": customer_points.points
        }
    )
    db.commit()
    return result

def delete_customer_points(customer_id: int, db: Session):
    result = db.query(schema.CustomerPoints).filter(
        schema.CustomerPoints.id == customer_id).delete()
    db.commit()
    return result