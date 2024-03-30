# WTF
# using flask wt-forms
# activate the venv
# run command 
# pip install flask-wtf

from flask_wtf import FlaskForm
# add SelectField
from wtforms import StringField, SubmitField, SelectField, DecimalField

class SimpleForms(FlaskForm):
   name=StringField("Name")
   submit = SubmitField("Enter")
   
   # http://wtforms.simplecodes.com/docs/0.6.1/fields.html
   tips = SelectField(u'Tip Percentage', 
   choices=[('15'), ('20'), 
   ('25'), ('30'), 
   ('35')])

   # choices is a list of tuples 
   # Tuple example ('cpp', 'C++')  
   # C++ is what user sees on form 
   # cpp is what gets passed to handler

   bill = DecimalField("How Much")