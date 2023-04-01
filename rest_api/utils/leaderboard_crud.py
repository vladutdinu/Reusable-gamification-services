from operator import and_
from sqlalchemy.orm import Session
from utils import customer_crud
from datetime import date
from schemas import schema
from models import model

def create_leaderboard(leaderboard: model.Leaderboard, db: Session):
    new_leaderboard = schema.Leaderboard(
        start_date = leaderboard.start_date,
        end_date = leaderboard.end_date
    )
    db.add(new_leaderboard)
    db.commit()
    db.refresh(new_leaderboard)
    return new_leaderboard

def get_leaderboard_result(current_date: date,  db: Session):
    leaderboard = db.query(schema.Leaderboard).filter(current_date <= schema.Leaderboard.end_date).filter(current_date >= schema.Leaderboard.start_date).first()
    customers = db.query(schema.Customer).all()
    result = model.LeaderboardResult(
        leaderboard_result = [model.LeaderboardObject(
            index = customer.id,
            name = customer.customer_id,
            points = customer_crud.get_customer_with_points_by_id(customer.customer_id, db).__dict__['points'].points
        ) for customer in customers],
        start_date = leaderboard.start_date,
        end_date = leaderboard.end_date
    )
    return result

def get_leaderboard(leaderboard_id: int, db: Session):
    leaderboard = db.query(schema.Leaderboard).filter(schema.Leaderboard.id == leaderboard_id).first()
    return leaderboard
    
def update_leaderboard(leaderboard: model.Leaderboard, db: Session):
    result = db.query(schema.Leaderboard).filter(schema.Leaderboard.id == leaderboard.id).update(
        {
           "start_date": leaderboard.start_date,
           "end_date": leaderboard.end_date
        }
    )
    db.commit()
    return result

def delete_leaderboard(leaderboard_id: int, db: Session):
    result = db.query(schema.Leaderboard).filter(schema.Leaderboard.id == leaderboard_id).delete()
    db.commit()
    return result

