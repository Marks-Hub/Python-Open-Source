
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import relationship
#from sqlalchemy import func

engine = create_engine('sqlite:///movie_quote.db')
#engine = create_engine('sqlite:///')
Base = declarative_base()

#####################################################################
# class to make a movie 
class Movie(Base):
   __tablename__ = 'movies'
   
   id = Column(String, primary_key=True)
   movieTitle = Column(String)
   movieYear = Column(String)
   quote_in = relationship("Quote") # note relationship added to imports above
   
#######################################################################
# class to make a Quote
# we assume a quote was in ONE movie   
class Quote(Base):
   __tablename__ = 'quotes'
   
   id = Column(Integer, primary_key=True)
   quoteText = Column(String)
   quoteChar = Column(String)
   quoteActor = Column(String)
   movie_id = Column(String, ForeignKey('movies.id'))
   # note: ForeignKey added to imports above
   # the argument of ForeignKey is a table.column  
   # note it's table name not class name

Base.metadata.create_all(engine)