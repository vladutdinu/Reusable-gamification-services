from sqlalchemy.orm import Session
from schemas import schema
from datetime import date
from models import model
import requests
import os
import json

def create_spinning_wheel(spinning_wheel: model.SpinningWheel, db: Session):
    new_spinning_wheel = schema.SpinningWheel(
        start_date = spinning_wheel.start_date,
        end_date = spinning_wheel.end_date
    )
    db.add(new_spinning_wheel)
    db.commit()
    db.refresh(new_spinning_wheel)
    return new_spinning_wheel

def get_spinning_wheel(wheel_id: int, db: Session):
    spinning_wheel = db.query(schema.SpinningWheel).filter(wheel_id == schema.SpinningWheel.id).first()
    return spinning_wheel

def get_spinning_wheel_with_rewards(current_date: date, db: Session):
    spinning_wheel = db.query(schema.SpinningWheel).filter(current_date <= schema.SpinningWheel.end_date).filter(current_date >= schema.SpinningWheel.start_date).first()
    products = [
        {
            "name": "p1"
        },
        {
            "name": "p2"
        },
        {
            "name": "p3"
        }
    ]#requests.get(os.environ['SHOP_URL']+"/product/all").json()
    wheel_rewards = model.SpinningWheelRewards(
        slice=[product['name'] for product in products],
        start_date = spinning_wheel.start_date,
        end_date = spinning_wheel.end_date
    )
    return wheel_rewards

def update_spinning_wheel(spinning_wheel: model.SpinningWheel, db: Session):
    result = db.query(schema.SpinningWheel).filter(schema.SpinningWheel.id == spinning_wheel.id).update(
        {
           "start_date": spinning_wheel.start_date,
           "end_date": spinning_wheel.end_date
        }
    )
    db.commit()
    return result

def delete_spinning_wheel(spinning_wheel_id: int, db: Session):
    result = db.query(schema.SpinningWheel).filter(schema.SpinningWheel.id == spinning_wheel_id).delete()
    db.commit()
    return result

