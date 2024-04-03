from sqlalchemy import create_engine
engine = create_engine('sqlite:///./planet.db')
#engine = create_engine('sqlite:///')

from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

from sqlalchemy import Column, Integer, String, Float  

class Artist(Base):
   __tablename__ = 'artistss'
   
   id = Column(Integer, primary_key=True)
   artists = Column(String)
   time = Column(String)
   title = Column(String)

Base.metadata.create_all(engine)

from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=engine)
session = Session()



import os
os.chdir(os.path.dirname(os.path.realpath(__file__)))

with open("NewWave.txt", "r") as f:
   for line in f:
      i=0
      if line.strip(): #ignoring blank lines 
         x = line.rstrip().split("|")
         songs = Artist(artists=x[0], time=x[1], title=x[2]) 
         session.add(songs)
session.commit()

query = session.query(Artist)
results = query.all()
for item in results:
   print ("id={} name={} length={} nameofSong={}".format(item.id, item.artists, item.time, item.title )) 