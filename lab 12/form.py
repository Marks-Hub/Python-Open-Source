# WTF using flask wt-forms

'''
   This demo focuses on WTF Radio Field 
   (group of radio buttons)
   With radio buttons the user chooses 
   one option from among several
'''

from flask_wtf import FlaskForm
from wtforms import SubmitField, RadioField, SelectMultipleField, widgets, SelectField
from wtforms.validators import InputRequired

# https://gist.github.com/doobeh/4668212
class MultiCheckboxField(SelectMultipleField):
    widget = widgets.ListWidget(prefix_label=False)
    option_widget = widgets.CheckboxInput()

class FG_Form(FlaskForm):


   salad = RadioField(u'Salad (no list style)', 
   choices=[('Iceberg'), ('Romaine'), ('Spring Mix'),('Spinach')],
   validators=[InputRequired(message="Choose a Salad!")])

   # will be assigned a style class using Jinja on HTML form
   fixing = MultiCheckboxField(u'Fixings', 
   choices=[('Chicken','Chicken'), ('Tuna','Tuna'), 
   ('Tofu','Tofu'), ('Ham','Ham'), 
   ('Peppers','Peppers'), ('Broccoli','Broccoli'),
   ('Carrots','Carrots'),('Cucumbers','Cucumbers')], 
   render_kw={'class':'no_bullets'}
   ) 
   
   # is assigned a style class right here in WTF
   dressing = SelectField(u'Dressing', 
   choices=[('Balsamic Vinaigrette', 'Balsamic Vinaigrette'),
   ('Caesar','Caesar'),
   ('Italian','Italian'),
   ('French','French'),
   ('Ranch','Ranch')])
   
   
   submit = SubmitField("Place Order")