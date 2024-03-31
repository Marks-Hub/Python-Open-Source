from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import relationship

#engine = create_engine('sqlite:///./art.db')
engine = create_engine('sqlite:///cars.db')    
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
Session = sessionmaker(bind=engine)
session = Session()

import json
import os
os.chdir(os.path.dirname(os.path.realpath(__file__)))

with open('static/data/item.json') as f:
   cars_vroom = json.load(f)
#print(cars_vroom)
# to have access to the list element and its index 
# you can use enumerate
for i, car_owner in enumerate(cars_vroom["Bulky_machines"]):
   #print("{} -- {} {}".format(i, car_owner["name"]))
   a_owner = Car_Manufacturer(brand=car_owner["brand"], 
   owner=car_owner["owner"]) 
   session.add(a_owner)
   session.flush()  
   # https://stackoverflow.com/questions/17325006/how-to-create-a-foreignkey-reference-with-sqlalchemy
   # flush the session so that the painter is assigned an id    
   
   for j, beep_beep in enumerate(cars_vroom["Bulky_machines"][i]["cars"]):
      # print("\t", chr(97+j), art["painters"][i]["paintings"][j]["title"])
      a_cars = Car(nameofCar=beep_beep["nameofCar"], Manufactur_year=beep_beep["Manufactur_year"])
      a_cars.Manufacturer_no = a_owner.id
      session.add(a_cars)

session.commit()

# Hard-coded artist data OWNERS
carOwners = Owner(ownerName="Josh Michael")
session.add(carOwners)
carOwners = Owner(ownerName="Mark Tom")
session.add(carOwners)
carOwners = Owner(ownerName="Tom hanks")
session.add(carOwners)
carOwners = Owner(ownerName="Molly Yogurt")
session.add(carOwners)
session.commit()
session.flush()

# Hard-coded artist data EMPLOYEES
employees = Employee(employeeName="Josh Michael", Manufacturer_no="1")
session.add(employees)
employees = Employee(employeeName="Mark Tom", Manufacturer_no="2")
session.add(employees)
employees = Employee(employeeName="Tom hanks", Manufacturer_no="1")
session.add(employees)
employees = Employee(employeeName="Molly Yogurt", Manufacturer_no="1")
session.add(employees)
session.commit()
session.flush()

# lennon & mccartney wrote I saw her standing there
session.execute(write_table.insert().values([(1, 1), (2, 1)]))
session.commit()
# lennon & mccartney wrote Misery
session.execute(write_table.insert().values([(1, 2), (2, 2)]))
session.commit()
# lennon & mccartney wrote Ask Me Why
session.execute(write_table.insert().values([(1, 6), (2, 6)]))
session.commit()
# harrison wrote Don't Bother Me
session.execute(write_table.insert().values([(3, 6)]))
session.commit()
# import os
# os.chdir(os.path.dirname(os.path.realpath(__file__)))