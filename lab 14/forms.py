# WTF
# using flask wt-forms
# run command 
# pip install flask-wtf

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, SubmitField
from wtforms import DecimalField
from wtforms.validators import InputRequired, Length, NumberRange

class XKCD(FlaskForm):
   # CATEGORIES
   
   chapter = DecimalField("Chapter Number", 
   validators=[InputRequired(), 
   NumberRange(min=1, max=2611, message="Not a valid wage.")])

      #SUBMIT
   submit = SubmitField("Enter")