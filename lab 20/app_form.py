# Defining a form for entering data to insert an artist 
# into our art database

from random import choices
from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, SelectField
from wtforms.validators import InputRequired, Length



#######################################################
# Class for inserting a painting
class Poem_Form(FlaskForm):

   poemss = StringField("Poem", 
   validators=[InputRequired(message="You must enter a poem"), Length(min=3, max=90, message="Title length must be between 2 and 60 characters")], 
   default="Untitled")

   poet_id = SelectField("Poet ID")
   #painter_id = QuerySelectField("Painter ID ", query_factory=)    
   
   submit = SubmitField("Insert Painting")