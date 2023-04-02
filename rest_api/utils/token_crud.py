from sqlalchemy.orm import Session
from schemas import schema
from models import model

def create_token(token: model.Token, db: Session):
    new_token = schema.Token(
        qr_code = token.qr_code,
        token = token.token
    )
    db.add(new_token)
    db.commit()
    db.refresh(new_token)
    return new_token

def get_token(token_id: int, db: Session):
    token = db.query(schema.Token).filter(schema.Token.id == token_id).first()
    return token
    
def update_token(token: model.Token, db: Session):
    result = db.query(schema.Token).filter(schema.Token.id == token.id).update(
        {
            "qr_code": token.qr_code,
            "token": token.token
        }
    )
    db.commit()
    return result

def delete_token(token_id: int, db: Session):
    result = db.query(schema.Token).filter(schema.Token.id == token_id).delete()
    db.commit()
    return result