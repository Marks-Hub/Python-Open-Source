# WTF using flask wt-forms

from flask_wtf import FlaskForm
from wtforms import SubmitField, RadioField, SelectMultipleField, widgets, BooleanField, HiddenField, SelectField
from wtforms.validators import InputRequired

import json
import os
os.chdir(os.path.dirname(os.path.realpath(__file__)))

# get burger choices from a data file -- rather than names & prices hard coded 
with open('static/data/sundae.json') as f:
   json_data = f.read()

FG_data = json.loads(json_data)  # json loads method

# list of choices
# choices = tuples including value passed to handler and what user sees  
iceCream_choices = []
flavor_choices = []
topping_choices = []
for scoop in FG_data["scoops"]:
    # make a choice start with list since tuple does
    # not support append method
    my_list=[] 
    # first part is what is passed behind the scenes
    my_list.append("{}|{}".format(scoop["name"],scoop["price"]))
    # second part is what user sees
    my_list.append(scoop["name"])
    # cast as a tuple
    my_tuple = tuple(my_list)
    # add to list of choices
    iceCream_choices.append(my_tuple)

for flav in FG_data["flavors"]:
    # make a choice start with list since tuple does
    # not support append method
    my_list=[] 
    # first part is what is passed behind the scenes
    my_list.append("{}".format(flav["name"]))
    # second part is what user sees
    my_list.append(flav["name"])
    # cast as a tuple
    my_tuple = tuple(my_list)
    # add to list of choices
    flavor_choices.append(my_tuple)

for top in FG_data["toppings"]:
    # make a choice start with list since tuple does
    # not support append method
    my_list=[] 
    # first part is what is passed behind the scenes
    my_list.append("{}".format(top["name"]))
    # second part is what user sees
    my_list.append(top["name"])
    # cast as a tuple
    my_tuple = tuple(my_list)
    # add to list of choices
    topping_choices.append(my_tuple)
print(iceCream_choices)
print(flavor_choices)
print(topping_choices)

# https://gist.github.com/doobeh/4668212
class MultiCheckboxField(SelectMultipleField):
    widget = widgets.ListWidget(prefix_label=False)
    option_widget = widgets.CheckboxInput()

class FG_Forms(FlaskForm):
   Scooops = RadioField(u'Scoop Number', 
   choices=iceCream_choices,
   validators=[InputRequired(message=" Choose a Scoop! ")],
   render_kw={'class':'nobullet'})
   # https://stackoverflow.com/questions/22084886/add-a-css-class-to-a-field-in-wtform

   Flavors = SelectField(u'Flavor', 
   choices=flavor_choices,
   validators=[InputRequired(message=" Choose a Flavor! ")],
   render_kw={'class':'nobullet'})
   # https://stackoverflow.com/questions/22084886/add-a-css-class-to-a-field-in-wtform

   Toppings = MultiCheckboxField(u'Toppings!', 
   choices=topping_choices,
   render_kw={'class':'nobullet'})
   # https://stackoverflow.com/questions/22084886/add-a-css-class-to-a-field-in-wtform


   submit = SubmitField("Place Order")