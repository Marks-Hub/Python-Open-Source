from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import relationship

#engine = create_engine('sqlite:///./art.db')
#comment out the connect line statement to activate the table to work. MARK OKINNNNNNNNNNNNN
engine = create_engine('sqlite:///cars.db',
connect_args={'check_same_thread': False})
    
Base = declarative_base()

#########################################################################
# A Painter creates MANY Paintings
# A Painting is created by ONE Painter
#
# This is a ONE-TO-MANY relationship
# The Painting will have a Foreign Key establishing its relationship to the Painter 

write_table = Table('write_table', Base.metadata,
    Column('owners_id', Integer, ForeignKey('owners.id')),
    Column('cars_id', Integer, ForeignKey('cars.id'))
)
##########################################################################
# Painter Class corresponds to painters table in database
class Car_Manufacturer(Base):
   __tablename__ = 'Bulky_machines'
   
   id = Column(Integer, primary_key=True)
   brand = Column(String)
   owner = Column(String)
   cars = relationship("Car")
   employ = relationship("Employee")
   
##########################################################################
# Painting Class corresponds to paintings table in database
class Car(Base):
   __tablename__ = 'cars'
   
   id = Column(Integer, primary_key=True)
   nameofCar = Column(String)
   Manufactur_year = Column(String)
   Manufacturer_no = Column(Integer, ForeignKey('Bulky_machines.id'))
   owned = relationship("Owner", secondary=write_table, viewonly=True)

class Owner(Base):
   __tablename__ = 'owners'
   
   id = Column(Integer, primary_key=True)
   ownerName = Column(String)
   own = relationship("Car", secondary=write_table, viewonly=True)
   

class Employee(Base):
   __tablename__ = 'Employees'
   
   id = Column(Integer, primary_key=True)
   employeeName = Column(String)
   Manufacturer_no = Column(Integer, ForeignKey('Bulky_machines.id'))
   # note: ForeignKey added to imports above
   # the argument of ForeignKey is a table.column  
   # note it's table name not class name
Base.metadata.create_all(engine)
# import os
# os.chdir(os.path.dirname(os.path.realpath(__file__)))