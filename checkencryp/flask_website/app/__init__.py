from unicodedata import name
from flask import Flask, render_template, request, redirect, url_for
import sqlite3 as db

app = Flask(__name__)

@app.route('/')
def index():
        return render_template("index.html")

@app.route("/loggedin", methods = ['POST', 'GET'])
def loggedin():
    if request.method == 'POST':
        user = request.form['user']
        passw = request.form['pass']

        conn = db.connect('credentials.db')
        conn.row_factory = db.Row
        
        cur = conn.cursor()
        rows = cur.execute("SELECT * FROM user").fetchall()

        conn.close()
        userR = rows['user']
        passwR = rows['password']
        
        return render_template('loggedin.html', user = userR, passw = passwR)

@app.route("/logout", methods = ['POST', 'GET'])
def logout():
    return redirect('/')