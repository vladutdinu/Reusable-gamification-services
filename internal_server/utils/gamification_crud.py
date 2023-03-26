from sqlalchemy.orm import Session
from schemas import schema
from models import model
def create_gamification(gamification: model.Gamification, db: Session):
    new_gamification = schema.Gamification(
        name=gamification.name,
        description=gamification.description,
        tier=gamification.tier
    )
    db.add(new_gamification)
    db.commit()
    db.refresh(new_gamification)
    return new_gamification

def get_gamification(gamification_id: int, db: Session):
    gamification = db.query(schema.Gamification).filter(schema.Gamification.id == gamification_id).first()
    return gamification

def update_gamification(gamification: model.Gamification, db: Session):
    result = db.query(schema.Gamification).filter(schema.Gamification.id == gamification.id).update(
        {
            "name": gamification.name,
            "description": gamification.description,
            "tier": gamification.tier
        }
    )
    db.commit()
    return result

def delete_gamification(gamification_id: int, db: Session):
    result = db.query(schema.Gamification).filter(schema.Gamification.id == gamification_id).delete()
    db.commit()
    return result

