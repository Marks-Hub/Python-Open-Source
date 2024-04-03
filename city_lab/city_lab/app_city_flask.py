import app_city_define as my_db

from sqlalchemy.orm import sessionmaker

from forms_city import Delete_Country_Form, Insert_Country_Form
from flask import Flask, render_template, url_for, request, redirect

Session = sessionmaker(bind=my_db.engine)
session = Session()
   

query = session.query(my_db.City)
results = query.all()
#for item in results:
#   print ("id={} name={} period={} distance={}".format(item.id, item.name, item.period, item.distance )) 
print(results)
result_dict = [u.__dict__ for u in results]
print(result_dict)

app = Flask(__name__)

app.config["SECRET_KEY"]='Where in the world?'

@app.route("/")
def myredirect():
   return redirect(url_for('country_table'))


@app.route('/planet_table')
def planet_table():
   return render_template('country_table.html', title="Planet Table", header="Planet Table", countries=result_dict)


@app.route('/country_datatable')
def country_datatable():
   return render_template('country_datatable.html', title="Planet DataTable", header="Planet DataTable", city=result_dict)

@app.route('/country_table')
def country_table():
   query = session.query(my_db.Country)
   results = query.all()
   result_dict = [u.__dict__ for u in results]
   #print(result_dict)
   return render_template('country_table.html', title="Country Table", header="Country Table", countries=result_dict)


@app.route('/country_delete', methods=['GET', 'POST'])
def country_delete():
   form = Delete_Country_Form()

   if form.is_submitted():
      result = request.form
      
      country_to_delete = session.query(my_db.Country).get(result["country_id"])
      #print("Going to delete")
      #print(country_to_delete.name)
      session.delete(country_to_delete)
      session.commit() 
      
      query = session.query(my_db.Country)
      results = query.all()
      result_dict = [u.__dict__ for u in results]
      
      return render_template('country_table.html', title="After Deletion", header="After Deletion", countries=result_dict)

   return render_template('country_delete.html', title="Delete Country Form", header="Delete Country Form", form=form)


@app.route('/country_insert', methods=['GET', 'POST'])
def country_insert():
   form = Insert_Country_Form()

   #if form.is_submitted():
   #print(form.validate_on_submit())
   if form.validate_on_submit():
      result = request.form
      a_painter = my_db.Country(id = result["id"], name = result["name"])
      session.add(a_painter)
      session.commit()  

      return render_template('country_insert_form_handler.html', title="Insert Artist Form Handler", header="Insert Artist Form handler", result=result)
   return render_template('country_insert_form.html', title="Insert Artist Form", header="Insert Artist Form", form=form)

if __name__ == "__main__":
   app.run(debug=True)   