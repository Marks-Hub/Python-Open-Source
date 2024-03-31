import Starbucks_define as my_db

from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=my_db.engine)
session = Session()

import json
import os
os.chdir(os.path.dirname(os.path.realpath(__file__)))

with open('static/data/starbucks.json') as f:
   starDrink = json.load(f)
   print(starDrink)

for i, Drinks in enumerate(starDrink["drinks"]):
   # print("{} -- {} {}".format(i, artist["firstName"], artist["lastName"]))
   a_painter = my_db.Drink(drink_name=Drinks["drink_name"], drink_cal=Drinks["drink_cal"], 
   drink_fat=Drinks["drink_fat"], drink_protein=Drinks["drink_protein"], 
   drink_caff=Drinks["drink_caff"], drink_desc=Drinks["drink_desc"], 
   drink_img=Drinks["drink_img"]) 
   session.add(a_painter)
   session.flush()  

session.commit()


#StarbuckDrinks = session.query(my_db.Drink).all()
#for artist in StarbuckDrinks:
   #print("id={} drink_name={} drink_cal={} drink_fat={} drink_protein={} drink_caff={} drink_desc={} drink_img={}".format(artist.id, artist.drink_name, 
   #artist.drink_cal, artist.drink_fat, artist.drink_protein, artist.drink_caff, artist.drink_desc, artist.drink_img))

   
query = session.query(my_db.Drink)
results = query.all()
for item in results:
   print ("id={} drink_name={} drink_cal={} drink_fat={} drink_protein={} drink_caff={} drink_desc={} drink_img={}".format(item.id, item.drink_name, 
   item.drink_cal, item.drink_fat, item.drink_protein, item.drink_caff, item.drink_desc, item.drink_img)) 