from sqlalchemy import create_engine
engine = create_engine('sqlite:///city.db?check_same_thread=False')
#engine = create_engine('sqlite:///')

from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

from sqlalchemy import Column, Integer, String, Float, ForeignKey  
from sqlalchemy.orm import relationship

class Country(Base):
   __tablename__ = 'country'
   
   id = Column(String, primary_key=True)
   name = Column(String)
   cities = relationship("City") # note relationship added to imports above

class City(Base):
   __tablename__ = 'city'
   
   id = Column(Integer, primary_key=True)
   name = Column(String)
   lat = Column(Float)
   long = Column(Float)
   population = Column(Integer)
   country_id = Column(String, ForeignKey('country.id'))

Base.metadata.create_all(engine)
