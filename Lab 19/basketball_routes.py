'''
   import the definitions from app_art_define 
   so that when the user supplies the data we 
   can instantiate a Painter and insert the data 
   into the table
'''
import basketball_define as my_db
from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=my_db.engine)
session = Session()

# WTF?
# using flask wt-forms
# run command 
# pip install flask-wtf

from app_Basketball_form import Basketball_Form
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
   return redirect(url_for('basketball_form'))

#POS_list = session.query(my_db.Basketball).all()
#POS_choices = []
#for item in POS_list:
   mylist=[]
   mylist.append(str(item.id))
   mylist.append("{}".format(item.POS) )
   my_tuple = tuple(mylist)
   POS_choices.append(my_tuple)
#print(POS_choices)
#session.commit()

##########################################################
@app.route('/basketball_form', methods=['GET', 'POST'])
def basketball_form():
   #form = Painting_Form(from_other=artist_choices)
   form = Basketball_Form()
   #form.POS.choices=POS_choices
   #form.painter_id.choices=[(1, "Fred"), (2, "Wilma") ]
   print(form.validate_on_submit())
   # KEPT COMING BACK AS INVALID
   if form.validate_on_submit():
   #if form.is_submitted():
      result = request.form
      
      a_basketball = my_db.Basketball(POS= result["POS"], name=result["name"], age = result["age"], WT=result["WT"], College=result["College"])
      session.add(a_basketball)
      session.commit() 
   
      return render_template('basketball_handler.html', title="Insertbasketball Form Handler", header="Insert basketball Form handler", result=result)

   return render_template('basketball_form.html', title="Insert basketball Form", header="nsert basketball Form", form=form)

if __name__ == "__main__":
   app.run(debug=True)