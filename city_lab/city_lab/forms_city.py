# WTF using flask wt-forms

from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, SelectField, DecimalField
from wtforms.validators import InputRequired, Length
#from wtforms.ext.sqlalchemy.fields import QuerySelectField

import app_city_define as my_db

from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind=my_db.engine)
session = Session()

country_list = session.query(my_db.Country).all()
country_choices = []
for item in country_list:
   mylist=[]
   mylist.append(str(item.id))
   mylist.append("{}".format(item.name) )
   my_tuple = tuple(mylist)
   country_choices.append(my_tuple)

class Delete_Country_Form(FlaskForm):
 
   country_id = SelectField("Country ", choices=country_choices)
     
   submit = SubmitField("Delete Country")


class Insert_Country_Form(FlaskForm):
 
   id = StringField("Country ")

   name = StringField("Country Name")
     
   submit = SubmitField("Insert Country")
