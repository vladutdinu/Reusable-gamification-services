from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from database import Base

class Tier(Base):
    __tablename__ = "tiers"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String)
    price = Column(Integer)

class Gamification(Base):
    __tablename__ = "gamifications"
    
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String)
    description = Column(String)
    tier = Column(Integer, ForeignKey("tiers.id"))

class Customer(Base):
    __tablename__ = "customers"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String)
    type = Column(String)
    tier_picked = Column(Integer, ForeignKey("tiers.id"))