'''
   import the definitions from app_art_define 
   so that when the user supplies the data we 
   can instantiate a Painter and insert the data 
   into the table
'''
import app_define as my_db
from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=my_db.engine)
session = Session()

# WTF?
# using flask wt-forms
# run command 
# pip install flask-wtf

from app_form import Poem_Form
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
   return redirect(url_for('poem_form'))

poet_list = session.query(my_db.Poet).all()
poet_choices = []
for item in poet_list:
   mylist=[]
   mylist.append(str(item.id))
   mylist.append("{}".format(item.name) )
   my_tuple = tuple(mylist)
   poet_choices.append(my_tuple)
print(poet_choices)
session.commit()

##########################################################
@app.route('/poem_form', methods=['GET', 'POST'])
def poem_form():
   #form = poem_form(from_other=artist_choices)
   form = Poem_Form()
   form.poet_id.choices=poet_choices
   #form.painter_id.choices=[(1, "Fred"), (2, "Wilma") ]
   print(form.validate_on_submit())
   # KEPT COMING BACK AS INVALID
   if form.validate_on_submit():
   #if form.is_submitted():
      result = request.form
      
      a_poem = my_db.Poem(poemss= result["poemss"])
      a_poem.poet_id = result["poet_id"]
      session.add(a_poem)
      session.commit() 
   
      return render_template('poem_handler.html', title="Insert poem Form Handler", header="Insert poem Form handler", result=result)

   return render_template('poem_form.html', title="Insert poem Form", header="Insert poem Form", form=form)



from app_form import Delete_Poem_Form
@app.route('/poem_delete', methods=['GET', 'POST'])
def poem_delete():
   form = Delete_Poem_Form()

   '''
   added check_same_thread=False in  app_planet_define.py 
   engine = create_engine('sqlite:///planet.db?check_same_thread=False')
   otherwise was getting thread issues
   '''

   # KEPT COMING BACK AS INVALID
   if form.validate_on_submit():
   #if form.is_submitted():
      result = request.form
      
      planet_to_delete = session.query(my_db.Poem).get(int(result["poem_id"]))
      print("Going to delete")
      print(planet_to_delete.poemss)
      session.delete(planet_to_delete)
      session.commit() 
      
   
      query = session.query(my_db.Poem)
      results = query.all()
      result_dict = [u.__dict__ for u in results]
      

      return render_template('delete_handler.html', title="After Deletion", header="After Deletion", poems=result_dict)

   return render_template('delete.html', title="Delete Planet Form", header="Delete Planet Form", form=form)
if __name__ == "__main__":
   app.run(debug=True)