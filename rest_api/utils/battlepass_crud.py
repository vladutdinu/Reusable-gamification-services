from sqlalchemy.orm import Session
from schemas import schema
from models import model
from datetime import date

def create_target(target: model.Target, db: Session):
    new_target = schema.Target(
        product_id=target.product_id,
        target_points=target.target_points,
        battlepass_id=target.battlepass_id
    )
    db.add(new_target)
    db.commit()
    db.refresh(new_target)
    return new_target

def get_target_by_id(target_id: int, db: Session):
    targets = db.query(schema.Target).filter(
        schema.Target.id == target_id).first()
    return targets

def get_targets(battlepass_id: int, db: Session):
    targets = db.query(schema.Target).filter(
        schema.Target.battlepass_id == battlepass_id).all()
    return targets

def update_target(target: model.Target, db: Session):
    result = db.query(schema.Target).filter(schema.Target.id == target.id).update(
        {
            "product_id": target.product_id,
            "target_points": target.target_points,
            "battlepass_id": target.battlepass_id
        }
    )
    db.commit()
    return result

def update_target_status(target: model.Target, status: int, db: Session):
    result = db.query(schema.Target).filter(schema.Target.id == target.id).update(
        {
            "done": status
        }
    )
    db.commit()
    return result

def delete_target(target_id: int, db: Session):
    result = db.query(schema.Target).filter(
        schema.Target.id == target_id).delete()
    db.commit()
    return result

def delete_target_by_battleplass_id(battlepass_id: int, db: Session):
    result = db.query(schema.Target).filter(
        schema.Target.battlepass_id == battlepass_id).delete()
    db.commit()
    return result

def create_battlepass(battlepass: model.Battlepass, db: Session):
    new_targets = schema.Battlepass(
        customer_id=battlepass.customer_id,
        start_date=battlepass.start_date,
        end_date=battlepass.end_date
    )
    db.add(new_targets)
    db.commit()
    db.refresh(new_targets)
    return new_targets

# def attach_targets(targets: model.Target, battlepass_id: int, db: Session):
#     battlepass = db.query(schema.Battlepass).filter(schema.Battlepass.id == battlepass_id).first()
#     try:
#         for target in targets:
#             create_target(target, battlepass.id)
#         return 1
#     except:
#         return 0

def get_battlepass(battlepass_id: int, db: Session):
    battlepass = db.query(schema.Battlepass).filter(
        schema.Battlepass.id == battlepass_id).first()
    return battlepass

def get_battlepass_by_date(current_date: date, db: Session):
    battlepass = db.query(schema.Battlepass).filter(current_date <= schema.Battlepass.end_date).filter(current_date >= schema.Battlepass.start_date).first()
    return battlepass

def get_battlepass_with_targes(current_date: date, db: Session):
    _battlepass = get_battlepass_by_date(current_date, db)
    _targets = get_targets(_battlepass.__dict__["id"], db)
    battlepass = model.BattlepassTarget(
        targets = [model.Target(**target.__dict__) for target in _targets],
        start_date = _battlepass.start_date,
        end_date = _battlepass.end_date
    )
    return battlepass

def update_battlepass(battlepass: model.Battlepass, db: Session):
    result = db.query(schema.Battlepass).filter(schema.Battlepass.id == battlepass.id).update(
        {
            "start_date": battlepass.start_date,
            "end_date": battlepass.end_date
        }
    )
    db.commit()
    return result

def delete_battlepass(battlepass_id: int, db: Session):
    battlepass = db.query(schema.Battlepass).filter(
        schema.Battlepass.id == battlepass_id).delete()
    targets = delete_target_by_battleplass_id(battlepass_id, db)
    db.commit()
    if battlepass and targets:
        return 1
    else:
        return 0