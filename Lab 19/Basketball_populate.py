'''
  This code will populate the tables defined in app_art_define
  Separating the populate code from the define code allows other 
  code to access the definitions without "re-populating" the 
  database tables
'''
import basketball_define as my_db
from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=my_db.engine)
session = Session()

#################################################################
#position = my_db.Basketball(POS="C")
#session.add(position)
#position = my_db.Basketball(POS="F")
#session.add(position)
#position = my_db.Basketball(POS="G")
#session.add(position)
#position = my_db.Basketball(POS="SG")
#session.add(position)
#position = my_db.Basketball(POS="SF")
#session.add(position)
#position = my_db.Basketball(POS="PF")
#session.add(position)
#position = my_db.Basketball(POS="PG")
#session.add(position)
#session.commit()
#session.flush()