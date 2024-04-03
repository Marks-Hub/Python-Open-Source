'''
   import the definitions from app_gmq_define 
   so that when the user supplies the data we 
   can instantiate a Movie and insert the data 
   into the table
'''
import app_mq_define as my_db
from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=my_db.engine)
session = Session()
#MARK OKIN
# WTF?
# using flask wt-forms
# run command 
# pip install flask-wtf

from forms_mq import Movie_Form
# note addition of request and redirect to list below
from flask import Flask, render_template, url_for, request, redirect
app = Flask(__name__)

# YOU NEED A SECRET_KEY
# A secret key that will be used for securely signing the 
# session cookie and be used for any other security 
# related needs by extensions or your application. It 
# should be a long random string of bytes, although 
# unicode is accepted too.
app.config["SECRET_KEY"]='rosebud'

####################################################################
# redirect the default route to the form for inserting a new group 
@app.route("/")
def myredirect():
   return redirect(url_for('movie_form'))

###################################################################
# route for inserting an group
@app.route('/movie_form', methods=['GET', 'POST'])
def movie_form():
   form = Movie_Form()

   #if form.is_submitted():
   #print(form.validate_on_submit())
   if form.validate_on_submit():
      result = request.form
      a_movie = my_db.Movie(id= result["movieCode"], 
      movieTitle=result["movieTitle"], 
      movieYear=result["movieYear"])
      session.add(a_movie)
      session.commit()  

      return render_template('movie_form_handler.html', title="Insert Movie Form Handler", 
      header="Insert Movie Form handler", result=result)
   return render_template('movie_form.html', title="Insert Movie Form", 
   header="Insert Movie Form", quotes=form)

from forms_mq import Delete_quote_Form
@app.route('/planet_delete', methods=['GET', 'POST'])
def planet_delete():
   forms = Delete_quote_Form()

   '''
   added check_same_thread=False in  app_planet_define.py 
   engine = create_engine('sqlite:///planet.db?check_same_thread=False')
   otherwise was getting thread issues
   '''

   # KEPT COMING BACK AS INVALID
   if forms.validate_on_submit():
   #if form.is_submitted():
      result = request.form
      
      planet_to_delete = session.query(my_db.Quote).get(int(result["quotes_id"]))
      print("Going to delete")
      print(planet_to_delete.quoteText)
      session.delete(planet_to_delete)
      session.commit() 
      
   
      query = session.query(my_db.Quote)
      results = query.all()
      result_dict = [u.__dict__ for u in results]
      

      return render_template('quote_delete_handler.html', title="After Deletion", header="After Deletion", quotes=result_dict)

   return render_template('quote_delete.html', title="Delete Planet Form", header="Delete Planet Form", forms=forms)

query = session.query(my_db.Quote)
results = query.all()
#for item in results:
#   print ("id={} name={} period={} distance={}".format(item.id, item.name, item.period, item.distance )) 
print(results)
result_dict = [u.__dict__ for u in results]
print(result_dict)

@app.route('/planet_table')
def planet_table():
   return render_template('quote_table.html', title="Planet Table", header="Planet Table", planets=result_dict)


@app.route('/planet_datatable')
def planet_datatable():
   return render_template('quotes_datatable.html', title="Planet DataTable", header="Planet DataTable", planet=result_dict)

if __name__ == "__main__":
   app.run(debug=True)