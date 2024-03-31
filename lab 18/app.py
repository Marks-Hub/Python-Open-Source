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
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import relationship
#from sqlalchemy import func

#engine = create_engine('sqlite:///./beatles.db')
engine = create_engine('sqlite:///Quote_author.db')
Base = declarative_base()


# Make the bridge table -- has foreign keys to two other tables
# note Table added to imports
# note write_table defined before classes that use it
write_table = Table('write_table', Base.metadata,
    Column('subjectss_id', Integer, ForeignKey('subjectss.id')),
    Column('quotess_id', Integer, ForeignKey('quotess.id'))
)

#################################################################
# ALBUM CLASS
class Author(Base):
   __tablename__ = 'aurthorss'
   
   id = Column(String, primary_key=True)
   name = Column(String)
   quoteses = relationship("Quote") # note relationship added to imports above

#################################################################
# SONG CLASS   
class Quote(Base):
   __tablename__ = 'quotess'
   
   id = Column(Integer, primary_key=True)
   quote_words = Column(String)
   aurthorss_id = Column(String, ForeignKey('aurthorss.id'))
   written_by = relationship("Subject", secondary=write_table, viewonly=True)

#################################################################
# ARTIST CLASS
class Subject(Base):
   __tablename__ = 'subjectss'
   
   id = Column(Integer, primary_key=True)
   subjects = Column(String)
   categorized = relationship("Quote", secondary=write_table, viewonly=True)

Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

import os
os.chdir(os.path.dirname(os.path.realpath(__file__)))

# load up Album data
with open("static/data/Authors.txt", "r") as f:
   for line in f:
      i=0
      if line.strip(): #ignoring blank lines 
         x = line.rstrip().split(",")
         album = Author(id=x[0], name=x[1]) 
         session.add(album)
session.commit()
session.flush()

# load up Song data
with open("static/data/Quotes.txt", "r") as f:
   for line in f:
      i=0
      if line.strip(): #ignoring blank lines 
         x = line.rstrip().split(",")
         song = Quote(quote_words=x[0], aurthorss_id=x[1]) 
         session.add(song)
session.commit()
session.flush()

# Hard-coded artist data 
beatle = Subject(subjects="Motivotional")
session.add(beatle)
beatle = Subject(subjects="Inspirational")
session.add(beatle)
beatle = Subject(subjects="Funny")
session.add(beatle)
beatle = Subject(subjects="Love")
session.add(beatle)
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
session.execute(write_table.insert().values([(3, 9)]))
session.commit()


first_quote = session.query(Quote).first()
print("{} is under the subjects ".format(first_quote.quote_words))
for person in first_quote.written_by:
   print(person.subjects)
print("")

Motivotional = session.query(Subject).first()
print("{} has the following quotes under it:".format(Motivotional.subjects))
for song in Motivotional.categorized:
   print(song.quote_words)

Author_quotes = session.query(Author).first()
print("{} has the following quotes under him:".format(Author_quotes.name))
for quotesss in Author_quotes.quoteses:
   print(quotesss.quote_words)