from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime
from database import Base

class CustomerPoints(Base):
    __tablename__ = 'customers_points'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True) 
    points= Column(Integer)
    current_points = Column(Integer)

class Customer(Base):
    __tablename__ = 'customers'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True) 
    customer_id= Column(Integer)
    points_id = Column(Integer, ForeignKey("customers_points.id"))

class Token(Base):
    __tablename__ = 'tokens'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True) 
    qr_code= Column(String)
    token= Column(String)

class Monster(Base):
    __tablename__ = 'monsters'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True) 
    name = Column(String)

class Quest(Base):
    __tablename__ = 'quests'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True) 
    customer_id= Column(Integer, ForeignKey("customers.id"))
    quest= Column(String)
    type= Column(String)
    quantity= Column(Integer)
    target_quantity= Column(Integer)
    product_id= Column(Integer)
    points= Column(Integer)
    start_date= Column(DateTime)
    end_date= Column(DateTime)
    done= Column(Integer, default=0)

class Coupon(Base):
    __tablename__ = 'coupons'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    customer_id= Column(Integer, ForeignKey("customers.id"))
    product_id= Column(Integer)
    description= Column(String)
    discount= Column(Integer)
    points_required= Column(Integer)
    code= Column(String)
    start_date= Column(DateTime)
    end_date= Column(DateTime)
    done= Column(Integer, default=0)
    active= Column(Integer, default=0)

class Target(Base):
    __tablename__ = 'targets'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True) 
    product_id= Column(Integer)
    target_points= Column(Integer)
    battlepass_id= Column(Integer, ForeignKey("battlepasses.id"))
    done= Column(Integer, default=0)

class Battlepass(Base):
    __tablename__ = 'battlepasses'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True) 
    customer_id= Column(Integer, ForeignKey("customers.id"))
    start_date= Column(DateTime)
    end_date= Column(DateTime)

class Leaderboard(Base):
    __tablename__ = 'leaderboards'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True) 
    start_date= Column(DateTime)
    end_date= Column(DateTime)

class SpinningWheel(Base):
    __tablename__ = 'spinningwheels'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True) 
    start_date= Column(DateTime)
    end_date= Column(DateTime)

class SpinningWheelRewards(Base):
    __tablename__ = 'spinningwheelrewards'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True) 
    product_id= Column(Integer)
    spinning_wheel_id= Column(Integer, ForeignKey("spinningwheels.id"))