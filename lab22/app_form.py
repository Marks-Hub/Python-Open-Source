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
   

import app_define as my_db

from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind=my_db.engine)
session = Session()

planet_list = session.query(my_db.Poem).all()
poem_choices = []
for item in planet_list:
   mylist=[]
   mylist.append(str(item.id))
   mylist.append("{}".format(item.poemss) )
   my_tuple = tuple(mylist)
   poem_choices.append(my_tuple)


class Delete_Poem_Form(FlaskForm):

   #painter_id = SelectField("Painter ID ", choices=[("1","Manet, Edouard"), ("2","Seurat, Georges")])
   poem_id = SelectField("poems ", choices=poem_choices)
   #painter_id = QuerySelectField("Painter ID ")    
   
   submit = SubmitField("Delete Planet")