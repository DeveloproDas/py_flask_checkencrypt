from unicodedata import name
from flask import Flask, render_template, request, redirect, url_for
#from app import app

app = Flask(__name__)

@app.route('/')
def index():
        return render_template("index.html")

@app.route("/loggedin", methods = ['POST', 'GET'])
def loggedin():
    if request.method == 'POST':
        user = request.form['user']
        passw = request.form['pass']
        return render_template('loggedin.html', user = user, passw = passw)

@app.route("/logout", methods = ['POST', 'GET'])
def logout():
    return redirect('/')