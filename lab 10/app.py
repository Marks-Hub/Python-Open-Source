# WTF?
# using flask wt-forms
# activate the venv 
# run command 
# pip install flask-wtf

# needs forms.py where SimpleForm class defined 
# needs simple_form.html where HTML of form generated
# needs simple_form_handler.html to display results
# needs simple_layout.htm and simple.css

from form import SimpleForms
# note addition of request and redirect to list below
from flask import Flask, render_template, url_for, request, redirect
app = Flask(__name__)

# YOU NEED A SECRET_KEY
# A secret key that will be used for securely signing the 
# session cookie and can be used for any other security 
# related needs by extensions or your application. It 
# should be a long random string of bytes, although 
# unicode is accepted too.
app.config["SECRET_KEY"]='why_a_duck?'


@app.route("/")
def my_redirect():
   return redirect(url_for('simple_form'))

@app.route('/formsTIp', methods=['GET', 'POST'])
def simple_form():
   form = SimpleForms()
   if form.is_submitted():
      result = request.form
      return render_template('handler.html', title="Restaurant calc", header="Restaurant Calc handler", result=result)
   return render_template('formsTIp.html', title="Restaurant calc", header="Restarant calc", form=form)

if __name__ == "__main__":
   app.run(debug=True)