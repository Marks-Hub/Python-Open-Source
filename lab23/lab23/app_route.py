'''
   Uses Flask to set up routes related to planet database
'''

import app as my_db

from sqlalchemy.orm import sessionmaker

from flask import Flask, render_template, url_for, request, redirect

Session = sessionmaker(bind=my_db.engine)
session = Session()

query = session.query(my_db.Artist)
results = query.all()
#for item in results:
#   print ("id={} name={} period={} distance={}".format(item.id, item.name, item.period, item.distance )) 
print(results)
result_dict = [u.__dict__ for u in results]
print(result_dict)

app = Flask(__name__)

app.config["SECRET_KEY"]='why_a_duck?'

######################### DEFAULT ROUTE REDIRECT ######################
@app.route("/")
def myredirect():
   return redirect(url_for('planet_api'))


import json
@app.route('/planet_api')
def planet_api():
   for item in result_dict:
      item.pop("_sa_instance_state", None)
   return json.dumps(result_dict)


if __name__ == "__main__":
   app.run(debug=True)   