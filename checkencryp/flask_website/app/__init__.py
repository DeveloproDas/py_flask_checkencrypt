from flask import Flask, render_template, request
#from app import app

app = Flask(__name__)

@app.route("/", methods = ['POST', 'GET'])
def index():
    if request.method == 'POST':
        user = request.form['user']
        passw = request.form['pass']
        return render_template('loggedin.html', user = user)
    else:
        return render_template('index.html')

@app.route("/loggedin", methods = ['POST', 'GET'])
def logon():
        return render_template('index.html')