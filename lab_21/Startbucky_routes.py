'''
   Uses Flask to set up routes related to planet database
'''

import Starbucks_define as my_db

from sqlalchemy.orm import sessionmaker

from flask import Flask, render_template, url_for, request, redirect

Session = sessionmaker(bind=my_db.engine)
session = Session()

query = session.query(my_db.Drink)
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
   return redirect(url_for('starbucks_table'))

@app.route('/starbucks_table')
def starbucks_table():
   return render_template('starbucks_table.html', title="Drinks Table", header="Starbucks Table", drinks=result_dict)


# route to datatable -- sorting and searching 
# note uses a different layout -- connects to jQuery JavaScript library
@app.route('/starbucks_datatable')
def starbucks_datatable():
   return render_template('starbucks_datatable.html', title="Planet Data Table", header="Planet Data Table", drinks=result_dict)


if __name__ == "__main__":
   app.run(debug=True)   