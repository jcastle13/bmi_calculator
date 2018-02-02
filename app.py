
from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/potato')
def welcome():
    return "This is my first Flask app! Yay!"

@app.route('/', methods=['GET', 'POST'])
def rootpage():
    name = ''
    if request.method == 'POST' and 'username' in request.form:
        name = request.form.get('username')
    return render_template("index.html", name = name)

@app.route('/bob')
def bobpage():
    return "Yo Bob! What's happning man!"


app.run()

