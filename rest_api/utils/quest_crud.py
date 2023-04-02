from sqlalchemy.orm import Session
from schemas import schema
from models import model
from utils import customer_crud

def create_quest(quest: model.Quest, db: Session):
    new_quest = schema.Quest(
        quest = quest.quest,
        quantity = quest.quantity,
        target_quantity = quest.target_quantity,
        product_id = quest.product_id,
        customer_id = quest.customer_id,
        type = quest.type,
        points = quest.points,
        start_date = quest.start_date,
        end_date = quest.end_date
    )
    db.add(new_quest)
    db.commit()
    db.refresh(new_quest)
    return new_quest

def get_quest(quest_id: int, db: Session):
    quest = db.query(schema.Quest).filter(schema.Quest.id == quest_id).first()
    return quest

def get_quests_customer(customer_id: int, db: Session):
    quests = db.query(schema.Quest).filter(schema.Quest.customer_id == customer_id).all()
    return quests

def update_quest(quest: model.Quest, db: Session):
    result = db.query(schema.Quest).filter(schema.Quest.id == quest.id).update(
        {
           "quest": quest.quest,
           "type": quest.type,
           "quantity": quest.quantity,
           "product_id": quest.product_id,
           "quantity": quest.quantity,
           "target_quantity": quest.target_quantity,
           "points": quest.points,
           "start_date": quest.start_date,
           "end_date": quest.end_date
        }
    )
    db.commit()
    _result = db.query(schema.Quest).filter(schema.Quest.id == quest.id).first()
    if _result.__dict__["quantity"] >= _result.__dict__["target_quantity"]:
        update_quest_status(_result, 1, db)
        _result = db.query(schema.Quest).filter(schema.Quest.id == quest.id).first()
        customer_points = customer_crud.get_customer_points(_result.__dict__['customer_id'], db)
        customer_points.current_points += _result.__dict__["points"]
        customer_points.points += _result.__dict__["points"]
        customer_crud.update_customer_points(customer_points, db)

    return _result

def update_quest_status(quest: model.Quest, status: int, db: Session):
    result = db.query(schema.Quest).filter(schema.Quest.id == quest.id).update(
        {
           "done": status
        }
    )
    db.commit()
    return result

def delete_quest(quest_id: int, db: Session):
    result = db.query(schema.Quest).filter(schema.Quest.id == quest_id).delete()
    db.commit()
    return result

