# WTF?
# using flask wt-forms
# run command 
# pip install flask-wtf

from form_cream import FG_Forms
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
def myredirct():
   return redirect(url_for('fg_form'))

@app.route('/forms', methods=['GET', 'POST'])
def fg_form():
   form = FG_Forms()

   #if form.is_submitted():
   #print(form.validate_on_submit())
   if form.validate_on_submit():
      result = request.form


      # https://stackoverflow.com/questions/13558345/flask-app-using-wtforms-with-selectmultiplefield
      print(result.getlist("toppings"))
      return render_template('form_handler.html', title="Sundae Form Handler", header="Sundae Form handler", result=result)
   return render_template('forms.html', title="Sundae Form", header="Sundae Form", form=form)

if __name__ == "__main__":
   app.run(debug=True)