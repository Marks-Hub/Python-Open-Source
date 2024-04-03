# Defining a form for entering data to insert an artist 
# into our art database

from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, TextAreaField, SelectField
from wtforms.validators import InputRequired, Length

#MARK OKIN
# Class for inserting an dog group 
class Movie_Form(FlaskForm):

   movieCode = StringField("Movie code: (3 or 4 characters)", 
   validators=[InputRequired(message="You must enter a 3-4 character code "), 
   Length(min=3, max=4, message="The code name must be between 3 and 4 characters")])

   movieTitle = StringField("Movie Title: ", 
   validators=[InputRequired(message="You must enter a movie title"), 
   Length(min=1, max=60, message="The movie title must be between 1 and 60 characters")])

   # for now we are requiring first and last name but that can cause issues  
   movieYear = StringField("Movie Year", 
   validators=[InputRequired(message="You must enter a movie year"), 
   Length(min=4, max=4, message="The movie year should be 4 digits")])
     
   submit = SubmitField("Insert a movie")

import app_mq_define as my_db

from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind=my_db.engine)
session = Session()

planet_list = session.query(my_db.Quote).all()
poem_choices = []
for item in planet_list:
   mylist=[]
   mylist.append(str(item.id))
   mylist.append("{}".format(item.quoteText) )
   my_tuple = tuple(mylist)
   poem_choices.append(my_tuple)


class Delete_quote_Form(FlaskForm):

   #painter_id = SelectField("Painter ID ", choices=[("1","Manet, Edouard"), ("2","Seurat, Georges")])
   quotes_id = SelectField("quotes ", choices=poem_choices)
   #painter_id = QuerySelectField("Painter ID ")    
   
   submit = SubmitField("Delete quote")