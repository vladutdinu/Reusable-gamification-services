import json
from sqlalchemy.orm import Session
from schemas import schema
from models import model
def create_user(user: model.User, db: Session):
    new_tier = schema.User(
       id=user.id,
       name=user.name,
       password=user.password,
       ranking=user.ranking
    )
    db.add(new_tier)
    db.commit()
    db.refresh(new_tier)
    return new_tier
def get_user(user_id: int, db: Session):
    user = db.query(schema.User).filter(schema.User.id == user_id).first()
    return user
def update_user(user: model.User, db: Session):
    result = db.query(schema.User).filter(schema.User.id == user.id).update(
        {
            "name":user.name,
            "password":user.password,
            "ranking":user.ranking
        }
    )
    db.commit()
    return result
def delete_user(user_id: int, db: Session):
    result = db.query(schema.User).filter(schema.User.id == user_id).delete()
    db.commit()
    return result