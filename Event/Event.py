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

engine = create_engine('sqlite:///event_MO.db')
#engine = create_engine('sqlite:///')
Base = declarative_base()

# Make the bridge table -- has foreign keys to two other tables
# note Table added to imports
# note write_table defined before classes that use it
write_table = Table('write_table', Base.metadata,
    Column('Staffs_id', Integer, ForeignKey('Staffs.id')),
    Column('Events_id', Integer, ForeignKey('Events.id'))
)

#################################################################
# ALBUM CLASS
class Customer(Base):
   __tablename__ = 'Customers'
   
   id = Column(String, primary_key=True)
   name = Column(String)
   phone = Column(String)
   email = Column(String)
   songs = relationship("Event") # note relationship added to imports above

#################################################################
# SONG CLASS   
class Staff(Base):
   __tablename__ = 'Staffs'
   
   id = Column(Integer, primary_key=True)
   name = Column(String)
   address = Column(String)
   written_by = relationship("Event", secondary=write_table, viewonly=True)

#################################################################
# ARTIST CLASS
class Event(Base):
   __tablename__ = 'Events'
   
   id = Column(Integer, primary_key=True)
   desc = Column(String)
   date = Column(String)
   time = Column(String)
   location = Column(String)
   Customera_id = Column(String, ForeignKey('Customers.id'))
   wrote = relationship("Staff", secondary=write_table, viewonly=True)


Session = sessionmaker(bind=engine)
session = Session()
Base.metadata.create_all(engine)
import os
os.chdir(os.path.dirname(os.path.realpath(__file__)))


# Hard-coded artist data 
customer = Customer(name="Mary Smith", phone="215-123-4567", email="smith_mary@gmail.com  ")
session.add(customer)
customer = Customer(name="Bob Jones", phone="215-321-7654", email="bob_jones@verizon.net")
session.add(customer)
session.commit()
session.flush()


staff = Staff(name="Fred Freed", address="809 Elm Street")
session.add(staff)
staff = Staff(name="Ginger Root", address="708 Oak Avenue")
session.add(staff)
staff = Staff(name="Wilma Rudolph", address="607 Pine Way")
session.add(staff)
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
