# WTF?
# using flask wt-forms
# run command 
# pip install flask-wtf

from form import FG_Form
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
def myredirect():
   return redirect(url_for('fg_form'))

@app.route('/fg_form', methods=['GET', 'POST'])
def fg_form():
   form = FG_Form()
   #if form.is_submitted():
   #print(form.validate_on_submit())
   if form.validate_on_submit():
      result = request.form
      return render_template('form_handler.html', title="Salad Form Handler", header="Salad Form handler", result=result)
   return render_template('forms.html', title="Salad Form", header="Salad Form", form=form)

if __name__ == "__main__":
   app.run(debug=True)