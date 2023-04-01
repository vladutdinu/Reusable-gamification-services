from sqlalchemy.orm import Session
from schemas import schema
from models import model

def create_monster(monster: model.Monster, db: Session):
    new_monster = schema.Monster(
        name = monster.name
    )
    db.add(new_monster)
    db.commit()
    db.refresh(new_monster)
    return new_monster

def get_monster(monster_name: str, db: Session):
    monster = db.query(schema.Monster).filter(schema.Monster.name == monster_name).first()
    return monster

def get_all_monsters(db: Session):
    monsters = db.query(schema.Monster).all()
    return monsters