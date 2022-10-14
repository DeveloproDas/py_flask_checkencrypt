#from unicodedata import name
from flask import Flask, render_template, request, redirect, url_for, abort, Response
import sqlite3 as sql
from sqlite3 import Error

app = Flask(__name__)

@app.route('/')
def index():
        return render_template("index.html")

@app.route("/loggedin", methods = ['POST', 'GET'])
def loggedin():
    if request.method == 'POST':
        user = request.form['user']
        passw = request.form['pass']
        
        try:
            conn = sql.connect('credentials.db')
            #conn.row_factory = sql.Row
            cur = conn.cursor()
            cur.execute("SELECT * FROM tableUser")
            rows = cur.fetchall()
            conn.close()
            for row in rows:
                userR = row[1]
                passwR = row[2]
        except Error as e:
            #abort(Response('User, Password or both are incorrect'))
            abort(Response('Database can not open.' +
            '<br><br><button onclick="history.back()">Back</button>'))
        if user == userR and passw == passwR:
            return render_template('loggedin.html', user = userR, passw = passwR)
        else:
            abort(Response('User or Password incorrects.' +
            '<br><br><button onclick="history.back()">Back</button>'))

@app.route("/logout", methods = ['POST', 'GET'])
def logout():
    return redirect('/')