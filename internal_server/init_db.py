from schemas import schema
from models import model
from database import SessionLocal, engine
from utils import customer_crud, gamification_crud, tier_crud

schema.Base.metadata.create_all(bind=engine)

from cryptography.fernet import Fernet
key = Fernet.generate_key()
with open("./secret.key", "wb") as key_file:
    key_file.write(key)

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

tiers = [
    {
        "name": "Simple gamification",
        "price": 100
    },
    {
        "name": "Average gamification",
        "price": 200
    },
    {
        "name": "Advanced gamification",
        "price": 300
    },
]

for tier in tiers:
    tier_crud.create_tier(model.Tier(
        name = tier["name"],
        price = tier["price"]
    ).copy(),  SessionLocal())

customers = [
    {
        "name": "C1",
        "type": "IT-Solutions",
        "tier_picked": 1
    },
    {
        "name": "C2",
        "type": "IT-Solutions",
        "tier_picked": 1
    },
    {
        "name": "C3",
        "type": "IT-Solutions",
        "tier_picked": 1
    },
    {
        "name": "C4",
        "type": "IT-Solutions",
        "tier_picked": 2
    },
    {
        "name": "C5",
        "type": "IT-Solutions",
        "tier_picked": 1
    },
    {
        "name": "C6",
        "type": "Coffe",
        "tier_picked": 1
    },
    {
        "name": "C7",
        "type": "Coffe",
        "tier_picked": 2
    },
    {
        "name": "C8",
        "type": "Coffe",
        "tier_picked": 2
    },
    {
        "name": "C9",
        "type": "Coffe",
        "tier_picked": 3
    },
    {
        "name": "C10",
        "type": "Coffe",
        "tier_picked": 2
    },
    {
        "name": "C11",
        "type": "Hotels",
        "tier_picked": 1
    },
    {
        "name": "C12",
        "type": "Hotels",
        "tier_picked": 3
    },
    {
        "name": "C13",
        "type": "Hotels",
        "tier_picked": 3
    },
    {
        "name": "C14",
        "type": "Hotels",
        "tier_picked": 3
    },
    {
        "name": "C15",
        "type": "Hotels",
        "tier_picked": 2
    }
]

for customer in customers:
    customer_model = model.Customer(
        name = customer['name'],
        type = customer['type'],
        tier_picked = customer['tier_picked'],
        token = encrypt_message(str({
            "name": customer['name'],
            "type": customer['type'],
            "tier_picked": customer['tier_picked']
        }))
    )
    customer_crud.create_customer(customer_model.copy(),  SessionLocal())

gamifications = [
    {
        "name": "Challenge",
        "description": "A challenge gamification feature that can be modified to fit for any product",
        "tier": 1
    },
    {
        "name": "Battlepass",
        "description": "A battlepass gamification feature that can be modified to fit multiple milestones and products",
        "tier": 2
    },
    {
        "name": "Survey",
        "description": "A survey gamification feature that can be modified to fit for any product and a template email",
        "tier": 1
    },
    {
        "name": "Spinning wheel",
        "description": "A spinning wheeln gamification feature that can be modified to fit multiple products (daily, weekly)",
        "tier": 2
    },
    {
        "name": "Leaderboard",
        "description": "A leaderboard gamification feature that can be modified to give a reward at a certain threshold",
        "tier": 2
    },
    {
        "name": "Pet",
        "description": "A pet gamification feature that can be used to reward the customer with items that can customize the personal pet",
        "tier": 3
    },
    {
        "name": "Coupon",
        "description": "A coupon reward feature that can be modified to offer the customer a discount",
        "tier": 1
    }
]

for gamification in gamifications:
    gamification_crud.create_gamification(model.Gamification(
        name = gamification["name"],
        description = gamification["description"],
        tier = gamification["tier"]
    ).copy(),  SessionLocal())