# WTF using flask wt-forms

from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, SelectField, DecimalField
from wtforms.validators import InputRequired, Length
#from wtforms.ext.sqlalchemy.fields import QuerySelectField

import app as my_db

from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind=my_db.engine)
session = Session()

planet_list = session.query(my_db.Song).all()
planet_choices = []
for item in planet_list:
   mylist=[]
   mylist.append(str(item.id))
   mylist.append("{}".format(item.title) )
   my_tuple = tuple(mylist)
   planet_choices.append(my_tuple)

#############################################################
class Update_song_Form(FlaskForm):
   
   song_id = SelectField("Song ", choices=planet_choices)

   artistss = StringField("artists Name")

   times =  StringField("Song time") 

   titles = StringField("Song title") 
   
   submit = SubmitField("Update Song")    

class Insert_song_Form(FlaskForm):
   artists = StringField("Artist", 
   validators=[InputRequired(message="You must enter a country"), 
   Length(min=2, max=60, message="Country length must be between 2 and 60 characters")])

   time = StringField("Length of song")

   title = StringField("Title")

   submit = SubmitField("Insert Artist")