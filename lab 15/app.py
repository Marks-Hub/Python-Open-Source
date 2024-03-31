# WTF?
# using flask wt-forms
# run command 
# pip install flask-wtf

from forms_relieve import Logon_Forms
# note addition of request and redirect to list below
from flask import Flask, render_template, url_for
from flask import request, redirect, session
app = Flask(__name__)

# YOU NEED A SECRET_KEY
app.config["SECRET_KEY"]='can_you_keep_a_secret?'

@app.route("/")
def myredirect():
   return redirect(url_for('forms'))

@app.route('/forms', methods=['GET', 'POST'])
def forms():
   form = Logon_Forms()
   #if form.is_submitted():
   #print(form.validate_on_submit())
   if form.validate_on_submit():
      print("oooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo0000000000000000000000000000000000000000000000000")
      result = request.form
      session["email"]=result['email']
      return render_template('form_handler.html', title="Welcome", header="Welcome", result=result)      
      #return redirect(url_for('welcome'))
   return render_template('forms.html', title="Logon Form", header="Please Logon", form=form)

@app.route('/welcome')
def welcome():
   if "email" in session:
      return render_template('form_handler.html', title="Welcome", header="Welcome")  
   else:
      return redirect(url_for('forms'))

if __name__ == "__main__":
   app.run(debug=True)