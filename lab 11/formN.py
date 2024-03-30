# WTF
# using flask wt-forms
# run command 
# pip install flask-wtf

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms import DecimalField
from wtforms.validators import InputRequired, Length, NumberRange

class SimpleForms(FlaskForm):
   # added a validator
   name=StringField("Name", 
   validators=[InputRequired(message="You must enter a name"), 
   Length(min=4, max=60, 
   message="Name length must be between 4 and 60 characters")])

   submit = SubmitField("Enter")
   # http://wtforms.simplecodes.com/docs/0.6.1/fields.html
   costOfFrames = SelectField(u'Frames', 
   choices=[('Silver with Gold Wood Picture Frame|1.10'), ('Dark Brown Wood Picture Frame|0.90'),
    ('Dark Brown Wood Picture Frame|0.90'), ('Espresso Wood Picture Frame|2.50'), ('Beaded Black Wood Picture Frame|1.20'), ('Black with Gold Leaf Wood Picture Frame|2.50')])
   
   width = DecimalField("Width", 
   validators=[InputRequired(), 
   NumberRange(min=8, max=96, message="Not a valid wage.")])

   length = DecimalField("Length", 
   validators=[InputRequired(), 
   NumberRange(min=8, max=96, message="Not a valid wage.")])
