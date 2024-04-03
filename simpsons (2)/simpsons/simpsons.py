'''
   In this version of the Beatles database we 
   have three classes/entities: Song, Album and Artist

   We have a one-to-many relationship between Song and Album 
      A Song is on ONE Album
      An Album has MANY Songs 

   We have a many-to-many relationship between Song and Artist
      A Song is written by MANY (more than one) Artists
      An Artist writes MANY Songs

   Many-to-Many relationships are made by having a "bridge table"
'''
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import relationship
#from sqlalchemy import func
from sqlalchemy import create_engine

engine = create_engine('sqlite:///simpsons_MO.db')
#engine = create_engine('sqlite:///')
Base = declarative_base()

# Make the bridge table -- has foreign keys to two other tables
# note Table added to imports
# note write_table defined before classes that use it
write_table = Table('write_table', Base.metadata,
    Column('characters_id', Integer, ForeignKey('characters.id')),
    Column('episodes_id', Integer, ForeignKey('episodes.id'))
)

#################################################################
# ALBUM CLASS
class Actor(Base):
   __tablename__ = 'actors'
   
   id = Column(String, primary_key=True)
   first_name = Column(String)
   last_name = Column(String)
   BDay = Column(String)
   songs = relationship("Character") # note relationship added to imports above

#################################################################
# SONG CLASS   
class Character(Base):
   __tablename__ = 'characters'
   
   id = Column(Integer, primary_key=True)
   first_name = Column(String)
   last_name = Column(String)
   actors_id = Column(String, ForeignKey('actors.id'))
   written_by = relationship("Episode", secondary=write_table, viewonly=True)

#################################################################
# ARTIST CLASS
class Episode(Base):
   __tablename__ = 'episodes'
   
   id = Column(Integer, primary_key=True)
   title = Column(String)
   orig_date = Column(String)
   wrote = relationship("Character", secondary=write_table, viewonly=True)


Session = sessionmaker(bind=engine)
session = Session()
Base.metadata.create_all(engine)
import os
os.chdir(os.path.dirname(os.path.realpath(__file__)))


# Hard-coded artist data 
VActor = Actor(first_name="Dan", last_name="Castellaneta", BDay="10/27/1957")
session.add(VActor)
VActor = Actor(first_name="Yeardly", last_name="Smith", BDay="7/3/1964")
session.add(VActor)
VActor = Actor(first_name="Nancy", last_name="Cartwright", BDay="10/25/1957")
session.add(VActor)
VActor = Actor(first_name="Julie", last_name="Kavner", BDay="9/7/1950")
session.add(VActor)
session.commit()
session.flush()


Chara = Character(first_name="Homer", last_name="Simpson")
session.add(Chara)
Chara = Character(first_name="Lisa", last_name="Simpson")
session.add(Chara)
Chara = Character(first_name="Bart", last_name="Simpson")
session.add(Chara)
Chara = Character(first_name="Marge", last_name="Simpson")
session.add(Chara)
Chara = Character(first_name="Ralph", last_name="Wiggum")
session.add(Chara)
Chara = Character(first_name="Barney", last_name="Gumble ")
session.add(Chara)
session.commit()
session.flush()

Episod = Episode(title="Simpsons Roasting on an Open Fire", orig_date="12/17/1989")
session.add(Episod)
Episod = Episode(title="Treehouse of Horror", orig_date="10/25/1990 ")
session.add(Episod)
session.commit()
session.flush()
# lennon & mccartney wrote I saw her standing there
session.execute(write_table.insert().values([(1, 1), (2, 1), (4, 1), (3, 1)]))
session.commit()
# lennon & mccartney wrote Misery
session.execute(write_table.insert().values([(1, 2), (2, 2), (4, 2), (3, 2)]))
session.commit()


#first_song = session.query(Song).first()
#print("{} was written by ".format(first_song.song_title))
#for person in first_song.written_by:
#   print(person.last_name)
#print("")

#john = session.query(Artist).first()
#print("{} wrote the following songs:".format(john.last_name))
#for song in john.wrote:
#   print(song.song_title)
