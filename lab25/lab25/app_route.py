'''
   Uses Flask to set up routes related to planet database
'''

import app as my_db

from sqlalchemy.orm import sessionmaker

from flask import Flask, render_template, url_for, request, redirect

Session = sessionmaker(bind=my_db.engine)
session = Session()

query = session.query(my_db.Song)
results = query.all()
#for item in results:
#   print ("id={} name={} period={} distance={}".format(item.id, item.name, item.period, item.distance )) 
print(results)
result_dict = [u.__dict__ for u in results]
print(result_dict)

app = Flask(__name__)

app.config["SECRET_KEY"]='why_a_duck?'


@app.route("/")
def myredirect():
   return redirect(url_for('app_table'))

######################### DEFAULT ROUTE REDIRECT ######################
import json
@app.route('/app_api')
def app_api():
   for item in result_dict:
      item.pop("_sa_instance_state", None)
   return json.dumps(result_dict)




########################## HTML TABLE ###############################
@app.route('/app_table')
def app_table():
   return render_template('app_table.html', title="Planet Table", header="Planet Table", song=result_dict)


########################### DATATABLE (SEARCH & SORT) #################
@app.route('/app_datatable')
def app_datatable():
   return render_template('app_datatable.html', title="Planet DataTable", header="Planet DataTable", song=result_dict)


###########################  DELETE ###################################


####################### UPDATE  #######################################
from app_form import Update_song_Form
@app.route('/app_update', methods=['GET', 'POST'])
def app_update():
   form = Update_song_Form()

   if form.is_submitted():
      result = request.form
      
      song_to_update = session.query(my_db.Song).get((result["song_id"]))
      print("Going to update")
      print(song_to_update.artists)

      song_to_update.artists = result["artistss"]
      song_to_update.time = result["times"]
      song_to_update.title = result["titles"]

      session.commit() 
         
      query = session.query(my_db.Song)
      results = query.all()
      result_dict = [u.__dict__ for u in results]
      
      return render_template('app_datatable.html', title="After Update", header="After Update", song=result_dict)

   return render_template('app_update.html', title="Crappy Update Planet Form", header="Crappy Update Planet Form", form=form)

from app_form import Insert_song_Form
@app.route('/app_form', methods=['GET', 'POST'])
def app_form():
   form = Insert_song_Form()

   #if form.is_submitted():
   #print(form.validate_on_submit())
   if form.validate_on_submit():
      result = request.form
      a_painter = my_db.Song(artists = result["artists"], time=result["time"], title=result["title"])
      session.add(a_painter)
      session.commit()  

      return render_template('app_form_handler.html', title="Insert Artist Form Handler", header="Insert Artist Form handler", result=result)
   return render_template('app_form.html', title="Insert Artist Form", header="Insert Artist Form", form=form)
if __name__ == "__main__":
   app.run(debug=True)   
if __name__ == "__main__":
   app.run(debug=True)   