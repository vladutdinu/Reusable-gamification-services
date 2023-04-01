from sqlalchemy.orm import Session
from schemas import schema
from datetime import date
from models import model
import requests
import os
import json
SHOP_URL = "http://localhost:8002"#os.environ['SHOP_URL']
def create_spinning_wheel(spinning_wheel: model.SpinningWheel, db: Session):
    new_spinning_wheel = schema.SpinningWheel(
        start_date = spinning_wheel.start_date,
        end_date = spinning_wheel.end_date
    )
    db.add(new_spinning_wheel)
    db.commit()
    db.refresh(new_spinning_wheel)
    return new_spinning_wheel

def create_spinning_wheel_reward(spinning_wheel_reward: model.SpinningWheelRewards, db: Session):
    new_spinning_wheel_reward = schema.SpinningWheelRewards(
        product_id = spinning_wheel_reward.product_id,
        spinning_wheel_id = spinning_wheel_reward.spinning_wheel_id
    )
    db.add(new_spinning_wheel_reward)
    db.commit()
    db.refresh(new_spinning_wheel_reward)
    return new_spinning_wheel_reward

def get_spinning_wheel(wheel_id: int, db: Session):
    spinning_wheel = db.query(schema.SpinningWheel).filter(wheel_id == schema.SpinningWheel.id).first()
    return spinning_wheel

def get_spinning_wheel_reward(wheel_id: int, db: Session):
    spinning_wheel = db.query(schema.SpinningWheelRewards).filter(wheel_id == schema.SpinningWheelRewards.spinning_wheel_id).first()
    return spinning_wheel

def get_spinning_wheel_rewards(wheel_id: int, db: Session):
    spinning_wheel = db.query(schema.SpinningWheelRewards).filter(wheel_id == schema.SpinningWheelRewards.spinning_wheel_id).all()
    return spinning_wheel


def get_spinning_wheel_with_rewards(current_date: date, db: Session):
    spinning_wheel = db.query(schema.SpinningWheel).filter(current_date <= schema.SpinningWheel.end_date).filter(current_date >= schema.SpinningWheel.start_date).first()
    _rewards = get_spinning_wheel_rewards(spinning_wheel.id, db)
    slices = []
    for reward in _rewards:
       result = requests.get(SHOP_URL+"/product/{}".format(reward.__dict__["product_id"])).json()
       result["reward_id"] = reward.__dict__["id"]
       slices.append(result)
    wheel_rewards = model.SpinningWheelRewards(
        slice=[model.SpinningWheelReward(
            id = _slice['reward_id'],
            name = _slice['name'],
            product_id = _slice['id'],
            spinning_wheel_id = spinning_wheel.id,
        ).__dict__ for _slice in slices],
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

def update_spinning_wheel_reward(spinning_wheel_reward: model.SpinningWheelRewards, db: Session):
    result = db.query(schema.SpinningWheelRewards).filter(schema.SpinningWheelRewards.id == spinning_wheel_reward.id).update(
        {
           "product_id": spinning_wheel_reward.product_id,
           "spinning_wheel_id": spinning_wheel_reward.spinning_wheel_id
        }
    )
    db.commit()
    return result

def delete_spinning_wheel(spinning_wheel_id: int, db: Session):
    result = db.query(schema.SpinningWheel).filter(schema.SpinningWheel.id == spinning_wheel_id).delete()
    db.commit()
    return result

def delete_spinning_wheel_reward(spinning_wheel_reward_id: int, db: Session):
    result = db.query(schema.SpinningWheelRewards).filter(schema.SpinningWheelRewards.id == spinning_wheel_reward_id).delete()
    db.commit()
    return result

