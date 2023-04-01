from sqlalchemy.orm import Session
from schemas import schema
from models import model

def create_quest(quest: model.Quest, db: Session):
    new_quest = schema.Quest(
        quest = quest.quest,
        quantity = quest.quantity,
        product_id = quest.product_id,
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
    
def update_quest(quest: model.Quest, db: Session):
    result = db.query(schema.Quest).filter(schema.Quest.id == quest.id).update(
        {
           "quest": quest.quest,
           "quantity": quest.quantity,
           "product_id": quest.product_id,
           "points": quest.points,
           "start_date": quest.start_date,
           "end_date": quest.end_date
        }
    )
    db.commit()
    return result

def delete_quest(quest_id: int, db: Session):
    result = db.query(schema.Quest).filter(schema.Quest.id == quest_id).delete()
    db.commit()
    return result

