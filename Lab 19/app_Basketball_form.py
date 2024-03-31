# Defining a form for entering data to insert an artist 
# into our art database

from random import choices
from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, SelectField
from wtforms.validators import InputRequired, Length



#######################################################
# Class for inserting a painting
class Basketball_Form(FlaskForm):

   #POS = SelectField("POS")
   POS = SelectField('POS', 
   choices=[('C'), ('F'), ('G'),('SG'), ('SF'),('PF'), ('PG')])

   name = StringField("name", 
   validators=[InputRequired(message="You must enter a poem"), Length(min=2, max=90, message="Title length must be between 2 and 60 characters")], 
   default="Untitled")

   age = StringField("age", 
   validators=[InputRequired(message="You must enter a poem"), Length(min=2, max=90, message="Title length must be between 2 and 60 characters")], 
   default="Untitled")
   
   WT = StringField("WT", 
   validators=[InputRequired(message="You must enter a poem"), Length(min=2, max=90, message="Title length must be between 2 and 60 characters")], 
   default="Untitled")

   College = StringField("College", 
   validators=[InputRequired(message="You must enter a poem"), Length(min=2, max=90, message="Title length must be between 2 and 60 characters")], 
   default="Untitled")
   
   
   submit = SubmitField("Insert basketbalal info")