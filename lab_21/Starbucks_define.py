'''
   Uses SQLAlchemy to define table for planets
'''

from sqlalchemy import create_engine
engine = create_engine('sqlite:///./drink.db')
#engine = create_engine('sqlite:///')

from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

from sqlalchemy import Column, Integer, String, Float  

class Drink(Base):
   __tablename__ = 'drinks'
   
   id = Column(Integer, primary_key=True)
   drink_name = Column(String)
   drink_cal = Column(Integer)
   drink_fat = Column(Integer)
   drink_protein = Column(Integer)
   drink_caff = Column(Integer)
   drink_desc = Column(String)
   drink_img = Column(String)

Base.metadata.create_all(engine)
