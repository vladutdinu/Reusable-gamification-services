import json
from sqlalchemy.orm import Session
from schemas import schema
from models import model
def create_user(user: model.User, db: Session):
    new_tier = schema.User(
       
       name=user.name,
       email=user.email,
       password=user.password,
       ranking=user.ranking
    )
    db.add(new_tier)
    db.commit()
    db.refresh(new_tier)
    return new_tier
def get_user_by_id(user_id: int, db: Session):
    user = db.query(schema.User).filter(schema.User.id == user_id).first()
    return user
def get_last_ranking( db: Session):
    try:
        ranking = db.query(schema.User).all()[-1].ranking
        return ranking
    except:
        return 0
def get_user_by_name(user_name: str, db: Session):
    user = db.query(schema.User).filter(schema.User.name == user_name).first()
    return user
def get_user_by_email(user_email: str, db: Session):
    user = db.query(schema.User).filter(schema.User.email == user_email).first()
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