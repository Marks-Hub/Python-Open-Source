'''
  This code will populate the tables defined in app_art_define
  Separating the populate code from the define code allows other 
  code to access the definitions without "re-populating" the 
  database tables
'''
import project_define as my_db
from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=my_db.engine)
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
   a_owner = my_db.Car_Manufacturer(brand=car_owner["brand"], 
   owner=car_owner["owner"]) 
   session.add(a_owner)
   session.flush()  
   # https://stackoverflow.com/questions/17325006/how-to-create-a-foreignkey-reference-with-sqlalchemy
   # flush the session so that the painter is assigned an id    
   
   for j, beep_beep in enumerate(cars_vroom["Bulky_machines"][i]["cars"]):
      # print("\t", chr(97+j), art["painters"][i]["paintings"][j]["title"])
      a_cars = my_db.Car(nameofCar=beep_beep["nameofCar"], Manufactur_year=beep_beep["Manufactur_year"])
      a_cars.Manufacturer_no = a_owner.id
      session.add(a_cars)

session.commit()

# Hard-coded artist data OWNERS
carOwners = my_db.Owner(ownerName="Josh Michael")
session.add(carOwners)
carOwners = my_db.Owner(ownerName="Mark Tom")
session.add(carOwners)
carOwners = my_db.Owner(ownerName="Tom hanks")
session.add(carOwners)
carOwners = my_db.Owner(ownerName="Molly Yogurt")
session.add(carOwners)
session.commit()
session.flush()

# Hard-coded artist data EMPLOYEES
employees = my_db.Employee(employeeName="Josh Michael", Manufacturer_no="1")
session.add(employees)
employees = my_db.Employee(employeeName="Mark Tom", Manufacturer_no="2")
session.add(employees)
employees = my_db.Employee(employeeName="Tom hanks", Manufacturer_no="1")
session.add(employees)
employees = my_db.Employee(employeeName="Molly Yogurt", Manufacturer_no="1")
session.add(employees)
session.commit()
session.flush()

# lennon & mccartney wrote I saw her standing there
session.execute(my_db.write_table.insert().values([(1, 1), (2, 1)]))
session.commit()
# lennon & mccartney wrote Misery
session.execute(my_db.write_table.insert().values([(1, 2), (2, 2)]))
session.commit()
# lennon & mccartney wrote Ask Me Why
session.execute(my_db.write_table.insert().values([(1, 6), (2, 6)]))
session.commit()
# harrison wrote Don't Bother Me
session.execute(my_db.write_table.insert().values([(3, 6)]))
session.commit()

query = session.query(my_db.Car_Manufacturer)
results = query.all()
for items in results:
   print ("id={} brand={} owner={}".format(items.id, items.brand, items.owner )) 
