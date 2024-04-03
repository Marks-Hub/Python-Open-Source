from forms_pers import PersForm
# note addition of request and redirect to list below
from flask import Flask, render_template, url_for, request, redirect
app = Flask(__name__)

app.config["SECRET_KEY"]='simon_and_garfunkel'

@app.route("/")
def myredirect():
   return redirect(url_for('form_pers'))

@app.route('/form_pers', methods=['GET', 'POST'])
def form_pers():
   form = PersForm()
   #if form.is_submitted():
   print(form.validate_on_submit())
   if form.validate_on_submit():
      result = request.form
      return render_template('form_handler_pers.html', title="MArk Okin Personality Form Handler", header="MArk Okin Personality Form handler", result=result)
   return render_template('form_pers.html', title="MArk Okin Personality Form", header="MArk Okin Personality Form", form=form)

if __name__ == "__main__":
   app.run(debug=True)