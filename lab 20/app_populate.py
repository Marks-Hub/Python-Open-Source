'''
  This code will populate the tables defined in app_art_define
  Separating the populate code from the define code allows other 
  code to access the definitions without "re-populating" the 
  database tables
'''
import app_define as my_db
from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=my_db.engine)
session = Session()

#################################################################
import json
import os
os.chdir(os.path.dirname(os.path.realpath(__file__)))

with open('static/data/poet.json') as f:
   art = json.load(f)

# to have access to the list element and its index 
# you can use enumerate
for i, poet_guy in enumerate(art["poets"]):
   # print("{} -- {} {}".format(i, artist["firstName"], artist["lastName"]))
   a_painter = my_db.Poet(name=poet_guy["name"]) 
   session.add(a_painter)
   session.flush()  
   # https://stackoverflow.com/questions/17325006/how-to-create-a-foreignkey-reference-with-sqlalchemy
   # flush the session so that the painter is assigned an id    
   
   for j, painting in enumerate(art["poets"][i]["poems"]):
      # print("\t", chr(97+j), art["painters"][i]["paintings"][j]["title"])
      a_poem = my_db.Poem(poemss=painting["poemss"])
      a_poem.poet_id = a_painter.id
      session.add(a_poem)

session.commit()