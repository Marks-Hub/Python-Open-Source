'''
   This Flask app used a common layout (HTML) and style (CSS) 
   for the pages in templates. 
   The layout being HTML is with the pages in the templates folder. 
   The style is in the static directory. 

   We use Jinja on the pages to distinguish between hard-coded 
   stuff and more dynamic stuff passed to the page(s).
'''
import json
import os
from flask import Flask, render_template, url_for, redirect
app = Flask(__name__)

# https://stackoverflow.com/questions/21133976/flask-load-local-json
filename = os.path.join(app.static_folder, 'data', 'noir.json')

with open(filename) as test_file:
    noir_data = json.load(test_file)

f = open(r"C:\Users\David\flask\Lab_9\c341_f21_Lab_09_Flask_Noir\static\data\noir_wiki.txt")

noir_txt = f.read()
f.close()         # close what you opened 
print(noir_txt)
print("\n_______________________________________________________\n")

'''
   We can pass multiple parameters to the pages. 
   Those passes parameters can be dictionaries. 
'''

@app.route('/')
def goToFirst():
   return redirect("/Films/") 

@app.route('/Films/')
def hello_world():
    return render_template('Films.html',
                           pass1={"name": "FRED", "occupation": "dancer"},
                           title="Noir Films", noir=noir_data)

# makes another page in a related but different location


@app.route('/About/')
def other():
    return render_template('About.html',
                           pass2={"name": "Ginger", "AboutFilm": noir_txt},
                           title="About Films")


# makes another page in a related but different location



# allows you to change and save changes to app.py
# and see them in the browser by refreshing
# without stopping and restarting the server
# only worked for me after I closed Visual Studio and re-opened (?)
if __name__ == "__main__":
    app.run(debug=True)
