from flask import Flask, render_template
app = Flask(__name__)

import json
import os 
os.chdir(os.path.dirname(os.path.realpath(__file__)))

with open('Sixers.json') as f:
   json_data = f.read()

Sixers = json.loads(json_data)  # json loads method
print(Sixers)  # list of dictionaries

@app.route('/')
@app.route('/About_me/')
def hello_world():
   return render_template('About_me.html')

@app.route('/Sixers/')
def flyer():
   return render_template('Sixers.html', players=Sixers)


if __name__ == "__main__":
   app.run(debug=True)