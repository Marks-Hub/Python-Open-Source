import app_city_define as my_db

from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=my_db.engine)
session = Session()

import os
os.chdir(os.path.dirname(os.path.realpath(__file__)))

#file = open(r'C:\path\to\your\filename.ext') 
with open(r'C:\Users\David\flask2\venv2\venv\static\data\Country.csv') as f:
   for line in f:
      i=0
      if line.strip(): #ignoring blank lines 
         x = line.rstrip().split(",")
         country = my_db.Country(name=x[0], id=x[1]) 
         session.add(country)
session.commit()

with open(r'C:\Users\David\flask2\venv2\venv\static\data\WorldCities.csv') as f:
   for line in f:
      i=0
      if line.strip(): #ignoring blank lines 
         x = line.rstrip().split(",")
         city = my_db.City(name=x[0], lat=float(x[1]), long=float(x[2]), country_id=x[3], population=int(x[4])) 
         session.add(city)
session.commit()

print("\n\nCountries\n")
query = session.query(my_db.Country)
results = query.all()
for item in results:
   print ("id={} name={}".format(item.id, item.name)) 

print("\n\nCities\n")
query = session.query(my_db.City)
results = query.all()
for item in results:
   print ("name={}, country_id={}".format( item.name, item.country_id))
