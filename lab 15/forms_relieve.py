# WTF using flask wt-forms
# Install email validator pip install email_validator

from email import message
from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, PasswordField, RadioField, SelectMultipleField, widgets

from wtforms.validators import InputRequired, Length, Email

class MultiCheckboxField(SelectMultipleField):
    widget = widgets.ListWidget(prefix_label=False)
    option_widget = widgets.CheckboxInput()

class Logon_Forms(FlaskForm):
   email =StringField("Email: ", 
   validators=[InputRequired(message="You must enter a name"), Length(min=4, max=30, message="Name length must be between 4 and 30 characters"),Email(message="Must be a valid email")])
   
   age = RadioField(u'Age Range', 
   choices=[('16-25', '16-25'), ('26-35', '26-35'), ('36-45', '36-45'), ('46-55', '46-55'), ('56-65', '56-65'), ('66- ', '66- '),],
   validators=[InputRequired(message="Choose a Range!")])

   reliever = MultiCheckboxField(u'Pain Reliever', 
   choices=[('Advil', 'Advil'), ('Aleve', 'Aleve'), ('Anacin', 'Anacin'), ('Bayer', 'Bayer'), ('Equate', 'Equate'), 
   ('Excedrin', 'Excedrin'), ('Motrin', 'Motrin'), ('Tylenol', 'Tylenol'), ('Generic', 'Generic')], 
   render_kw={'class':'no_bullets'}
   )

   submit = SubmitField("Submit my Survey")