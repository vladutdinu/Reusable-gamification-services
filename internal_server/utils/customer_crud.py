from sqlalchemy.orm import Session
from schemas import schema
from models import model

def create_customer(customer: model.Customer, db: Session):
    new_customer = schema.Customer(
        name=customer.name,
        type=customer.type,
        tier_picked=customer.tier_picked
    )
    db.add(new_customer)
    db.commit()
    db.refresh(new_customer)
    return new_customer

def get_customer(customer_id: int, db: Session):
    customer = db.query(schema.Customer).filter(schema.Customer.id == customer_id).first()
    return customer

def get_customer(customer_name: str, db: Session):
    customer = db.query(schema.Customer).filter(schema.Customer.name == customer_name).first()
    return customer

def get_customers_tiers_type(db: Session):
    customers = db.query(schema.Customer).all()
    tiers = db.query(schema.Tier).all()
    unique_business_types = list(set(customer.__dict__['type'] for customer in customers))
    tier_statistics = {}

    for business_type in unique_business_types:
        tier_statistics[business_type] = {}
        for tier in tiers:
            tier_statistics[business_type][tier.__dict__['id']] = 0

    for customer in customers:
        tier_statistics[customer.__dict__['type']][customer.__dict__['tier_picked']] += 1 

    return tier_statistics

def update_customer(customer: model.Customer, db: Session):
    result = db.query(schema.Customer).filter(schema.Customer.id == customer.id).update( {
            "name": customer.name,
            "type": customer.type,
            "tier_picked": customer.tier_picked
        })
    db.commit()
    return result

def delete_customer(customer_id: int, db: Session):
    result = db.query(schema.Customer).filter(schema.Customer.id == customer_id).delete()
    db.commit()
    return result

