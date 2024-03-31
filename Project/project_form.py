# Defining a form for entering data to insert an artist 
# into our art database

from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, SelectField
from wtforms.validators import InputRequired, Length

# Class for inserting an artist 
class manufacturer_Form(FlaskForm):
   brand = StringField("Car brand/Manufacturer", 
   validators=[InputRequired(message="You must enter a Car brand/Manufacturer"), 
   Length(min=2, max=60, message="Last Name length must be between 2 and 60 characters")])

   # for now we are requiring first and last name but that can cause issues  
   owner = StringField("Owner of brand/manufacturer", 
   validators=[InputRequired(message="You must enter a brand/manufacturer"), 
   Length(min=2, max=60, message="First Name length must be between 2 and 60 characters")])

     
   submit = SubmitField("Insert Manufacturer info")

class car_Form(FlaskForm):

   nameofCar = StringField("Name of Car", 
   validators=[InputRequired(message="You must enter a title"), Length(min=2, max=60, message="Title length must be between 2 and 60 characters")], 
   default="Untitled")
     
   Manufactur_year = StringField("Manufactur year", 
   validators=[InputRequired(message="You must enter a file name"), Length(min=2, max=60, message="File name length must be between 2 and 60 characters")], 
   default="default.jpg")

   #painter_id = SelectField("Painter ID ", choices=[("1","Manet, Edouard"), ("2","Seurat, Georges")])
   Manufacturer_no = SelectField("Manufacturer_no ID ")
   #painter_id = QuerySelectField("Painter ID ", query_factory=)    
   
   submit = SubmitField("Insert Painting")