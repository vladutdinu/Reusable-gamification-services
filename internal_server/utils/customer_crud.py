import json
from sqlalchemy.orm import Session
from schemas import schema
from models import model
from cryptography.fernet import Fernet
def load_key():
    """
    Load the previously generated key
    """
    return open("secret.key", "rb").read()

def encrypt_message(message):
    """
    Encrypts a message
    """
    key = load_key()
    encoded_message = message.encode()
    f = Fernet(key)
    encrypted_message = f.encrypt(encoded_message)

    return encrypted_message.decode()

def decrypt_message(encrypted_message):
    """
    Decrypts an encrypted message
    """
    key = load_key()
    f = Fernet(key)
    decrypted_message = f.decrypt(encrypted_message)

    return decrypted_message.decode()

def create_customer(customer: model.Customer, db: Session):
    new_customer = None
    if customer.token != "":
        new_customer = schema.Customer(
            name=customer.name,
            type=customer.type,
            tier_picked=customer.tier_picked,
            token=customer.token
        )
    else:
        new_customer = schema.Customer(
            name=customer.name,
            type=customer.type,
            tier_picked=customer.tier_picked
     )
    db.add(new_customer)
    db.commit()
    db.refresh(new_customer)
    return new_customer

def get_customer_by_id(customer_id: int, db: Session):
    customer = db.query(schema.Customer).filter(schema.Customer.id == customer_id).first()
    return customer

def get_customer_by_name(customer_name: str, db: Session):
    customer = db.query(schema.Customer).filter(schema.Customer.name == customer_name).first()
    return customer

def validate_token(validate: model.Validate, db: Session):
    customer = get_customer_by_id(validate.customer_id, db)
    if customer.token.encode("utf-8") == validate.token.encode("utf-8"):
        message = decrypt_message(validate.token.encode("utf-8"))
        return json.loads(message.replace("'",'"'))['tier_picked']
    return 0
    

def get_customers_tiers_type(db: Session):
    customers = db.query(schema.Customer).all()
    tiers = db.query(schema.Tier).all()
    unique_business_types = list(set(customer.__dict__['type'] for customer in customers))
    tier_statistics = {}

    for business_type in unique_business_types:
        tier_statistics[business_type] = {}
        for tier in tiers:
            tier_statistics[business_type][tier.__dict__['id']] = 0

    for customer in customers:
        tier_statistics[customer.__dict__['type']][customer.__dict__['tier_picked']] += 1 

    return tier_statistics

def get_customer_tier(token: str, db: Session):
    decoded_token = json.loads(decrypt_message(token).replace("'",'"'))
    customer = db.query(schema.Customer).filter(schema.Customer.name == decoded_token['name']).first()
    return customer

def update_customer(customer: model.Customer, db: Session):
    result = db.query(schema.Customer).filter(schema.Customer.id == customer.id).update( {
            "name": customer.name,
            "type": customer.type,
            "tier_picked": customer.tier_picked,
            "token": customer.token
        })
    db.commit()
    return result

def delete_customer(customer_id: int, db: Session):
    result = db.query(schema.Customer).filter(schema.Customer.id == customer_id).delete()
    db.commit()
    return result

