'''
   import the definitions from app_art_define 
   so that when the user supplies the data we 
   can instantiate a Painter and insert the data 
   into the table
'''
import project_define as my_db
from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=my_db.engine)
session = Session()


# WTF?
# using flask wt-forms
# run command 
# pip install flask-wtf

from project_form import manufacturer_Form, car_Form
# note addition of request and redirect to list below
from flask import Flask, render_template, url_for, request, redirect
app = Flask(__name__)

# YOU NEED A SECRET_KEY
# A secret key that will be used for securely signing the 
# session cookie and be used for any other security 
# related needs by extensions or your application. It 
# should be a long random string of bytes, although 
# unicode is accepted too.
app.config["SECRET_KEY"]='why_a_duck?'

####################################################################
# redirect the default route to the form for inserting a new artist 
@app.route("/")
def myredirect():
   return redirect(url_for('artist_form'))

###################################################################
# route for inserting an artist
@app.route('/artist_form', methods=['GET', 'POST'])
def artist_form():
   form = manufacturer_Form()

   #if form.is_submitted():
   #print(form.validate_on_submit())
   if form.validate_on_submit():
      result = request.form
      a_manufacturer = my_db.Car_Manufacturer(brand= result["brand"], owner=result["owner"])
      session.add(a_manufacturer)
      session.commit()  

      return render_template('project_handler.html', title="Insert manufacturer info Form Handler", header="Insert manufacturer info Form handler", result=result)
   return render_template('form.html', title="Insert manufacturer Form", header="Insert manufacturer Form", form=form)


########################################################################
manufacturer_list = session.query(my_db.Car_Manufacturer).all()
manufacturer_choices = []
for item in manufacturer_list:
   mylist=[]
   mylist.append(str(item.id))
   mylist.append("{}, {}".format(item.brand, item.owner) )
   my_tuple = tuple(mylist)
   manufacturer_choices.append(my_tuple)
print(manufacturer_choices)
session.commit()

##########################################################
@app.route('/painting_form', methods=['GET', 'POST'])
def painting_form():
   #form = Painting_Form(from_other=artist_choices)
   form = car_Form()
   form.Manufacturer_no.choices=manufacturer_choices
   #form.painter_id.choices=[(1, "Fred"), (2, "Wilma") ]
   print(form.validate_on_submit())
   # KEPT COMING BACK AS INVALID
   if form.validate_on_submit():
   #if form.is_submitted():
      result = request.form
      
      a_car = my_db.Car(nameofCar= result["nameofCar"], Manufactur_year=result["Manufactur_year"] )
      a_car.Manufacturer_no = result["Manufacturer_no"]
      session.add(a_car)
      session.commit() 
   
      return render_template('car_form_handler.html', title="Insert car Form Handler", header="Insert car Form handler", result=result)

   return render_template('car_form.html', title="Insert car Form", header="Insert car Form", form=form)

##########################################################
query = session.query(my_db.Car_Manufacturer)
results = query.all()

print(results)
result_dict = [u.__dict__ for u in results]
print(result_dict)

@app.route('/planet_table')
def planet_table():
   return render_template('tables.html', title="Table", header="Table", Bulky_machines=result_dict)

if __name__ == "__main__":
   app.run(debug=True)