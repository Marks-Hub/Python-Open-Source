'''
  This code will populate the tables defined in app_art_define
  Separating the populate code from the define code allows other 
  code to access the definitions without "re-populating" the 
  database tables
'''
import app_mq_define as my_db
from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=my_db.engine)
session = Session()

#################################################################
import os
os.chdir(os.path.dirname(os.path.realpath(__file__)))


# load Movie data from text file
with open("static/data/Movie.txt", "r") as f:
   for line in f:
      i=0
      if line.strip(): #ignoring blank lines 
         x = line.rstrip().split("|")
         a_record = my_db.Movie(id=x[0], movieTitle=x[1], movieYear=x[2]) 
         session.add(a_record)
session.commit()
session.flush()

# load Quote data from text file
with open("static/data/MovieQuotes.txt", "r") as f:
   for line in f:
      i=0
      if line.strip(): #ignoring blank lines 
         x = line.rstrip().split("|")
         a_record = my_db.Quote(id=int(x[0]), quoteText=x[1], quoteChar=x[2], quoteActor=x[3], movie_id=x[4]) 
         session.add(a_record)
session.commit()
session.flush()

#########################################################################
# query about the movie Casablanca
query = session.query(my_db.Movie).filter(my_db.Movie.id=="CSBL")
my_movie = query.first()
print ("id={} title={} year={}".format(my_movie.id, my_movie.movieTitle, 
my_movie.movieYear )) 

for my_quote in my_movie.quote_in:
   print(my_quote.quoteText)