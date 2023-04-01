import json
from sqlalchemy.orm import Session
from schemas import schema
from models import model
def create_type(type: model.Type, db: Session):
    new_tier = schema.Type(
       id=type.id,
       typeOf=type.typeOf

    )
    db.add(new_tier)
    db.commit()
    db.refresh(new_tier)
    return new_tier
def get_type(type_id: int, db: Session):
    type = db.query(schema.Type).filter(schema.Type.id == type_id).first()
    return type
def update_type(type: model.Type, db: Session):
    result = db.query(schema.Type).filter(schema.Type.id == type.id).update(
        {
            "id":type.id,
            "typeOf":type.typeOf

        }
    )
    db.commit()
    return result
def delete_type(type_id: int, db: Session):
    result = db.query(schema.Type).filter(schema.Type.id == type_id).delete()
    db.commit()
    return result