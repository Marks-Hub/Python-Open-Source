# WTF
# using flask wt-forms
# run command 
# pip install flask-wtf

from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, PasswordField, RadioField, SelectMultipleField, widgets, SelectField

from wtforms.validators import InputRequired, Length, Email

class MultiCheckboxField(SelectMultipleField):
    widget = widgets.ListWidget(prefix_label=False)
    option_widget = widgets.CheckboxInput()

class PersForm(FlaskForm):
   email=StringField("Email: ", 
   validators=[InputRequired(message="You must enter a name"), Length(min=4, max=30, message="Name length must be between 4 and 30 characters"),Email(message="Must be a valid email")])
   

   response = RadioField(u'Id rather be a sparrow than a snail', 
   choices=[('Strongly Agree', '1'), ('Agree', '2'), ('Neutral', '3'), ('Disagree', '4'), ('Strongly Disagree', '5')],
   validators=[InputRequired(message="Choose a Range!")])


   moreResponses = MultiCheckboxField(u'More responses', 
   choices=[("Aloof|", "Aloof"), ("Artistic", "Artistic"), ("Bland", "Bland"), 
   ("Brave", "Brave"), ("Clever", "Clever"), ("Critical", "Critical"), ("Dependable", "Dependable"), ("Dogmatic", "Dogmatic")], 
   render_kw={'class':'no_bullets'}
   )

   choices = SelectField(u'choice', 
   choices=[("Introverted", "Introverted"), ("Extraverted", "Extraverted")])
   submit = SubmitField("Enter")
