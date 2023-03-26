from sqlalchemy.orm import Session
from schemas import schema
from models import model
def create_tier(tier: model.Tier, db: Session):
    new_tier = schema.Tier(
        name = tier.name,
        price = tier.price
    )
    db.add(new_tier)
    db.commit()
    db.refresh(new_tier)
    return new_tier

def get_tier(tier_id: int, db: Session):
    tier = db.query(schema.Tier).filter(schema.Tier.id == tier_id).first()
    return tier
    
def update_tier(tier: model.Tier, db: Session):
    result = db.query(schema.Tier).filter(schema.Tier.id == tier.id).update(
        {
            "name": tier.name,
            "price": tier.price
        }
    )
    db.commit()
    return result

def delete_tier(tier_id: int, db: Session):
    result = db.query(schema.Tier).filter(schema.Tier.id == tier_id).delete()
    db.commit()
    return result

