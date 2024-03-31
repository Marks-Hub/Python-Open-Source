import json
from urllib.request import Request, urlopen

from forms import XKCD
# note addition of request and redirect to list below
from flask import Flask, render_template, url_for, request, redirect
from flask import redirect, make_response, session
app = Flask(__name__)

app.config["SECRET_KEY"]='why_a_duck?'

@app.route("/")
def myrediret():
   return redirect(url_for('nobel_forms'))

@app.route('/forms', methods=['GET', 'POST'])
def nobel_forms():
   form = XKCD()
   if form.is_submitted():
      result = request.form

      url = "http://xkcd.com/"+result["chapter"]+"/info.0.json"
      print(url)
      req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
      data = urlopen(req).read()
      XKCD_info = json.loads(data)
      session["chapter"]=result['chapter']

      resp = make_response(render_template('form_handler.html', 
      title="Nobel Form Handler", header="Nobel Form handler", 
      result=result, XKCD_info=XKCD_info))
      resp.set_cookie('chapter', result['chapter'])
      # longer shelf life (two days?)
      resp.set_cookie('chapter_2', result['chapter'], max_age=24*60*60*14)

      return resp
     
   return render_template('form_XKCD.html', title="XKCD Form", header="XKCD Form", form=form)

if __name__ == "__main__":
   app.run(debug=True)