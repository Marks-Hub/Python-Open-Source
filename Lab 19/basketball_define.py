'''
   We are going to start interfacing with the database (adding Flask).
   
   We will separate the code that 
   1. defines the database
   2. initially populates the tables
   3. controls the forms for a user to add additional artists 

   That way all other code can import the definitions 
   Also that way we can run the "populate code" once 
   But can run the user-insert code over and over
'''

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import relationship
#from sqlalchemy import func

engine = create_engine('sqlite:///basketball.db')
#engine = create_engine('sqlite:///')
Base = declarative_base()

#####################################################################
# class to make a Painter
class Basketball(Base):
   __tablename__ = 'poets'
   
   id = Column(Integer, primary_key=True)
   POS = Column(String)
   name = Column(String)
   age = Column(String)
   WT = Column(String)
   College = Column(String)


Base.metadata.create_all(engine)