from flask import Flask, render_template, Markup
import time
import sqlite3
from . import app

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/temperature')
def tempi():
    temp_list = []
    db = sqlite3.connect("temp.db", detect_types=sqlite3.PARSE_DECLTYPES)
    cursor_db = db.cursor()
    try:
        search_action = cursor_db.execute('SELECT date, temp FROM data')
    except sqlite3.OperationalError:
        print("\n\n DATABASE DOES NOT EXIST. MADE ONE INSTEAD. \n\n")
        cursor_db.execute('CREATE TABLE "data" (date TEXT NOT NULL,temp INTEGER NOT NULL);')
        search_action = cursor_db.execute('SELECT date, temp FROM data')
    for row in search_action:
        temp_list.append(row)

    db.close()
    try:
        currtemp = temp_list[-1][1]
    except IndexError:
        currtemp = None
    return render_template('tempi.html', temp_list=temp_list, currtemp=currtemp)

@app.route('/graph')
def graph():
    graphdata = []
    labels = []
    db = sqlite3.connect("temp.db", detect_types=sqlite3.PARSE_DECLTYPES)
    cursor_db = db.cursor()
    try:
        search_action = cursor_db.execute('SELECT date, temp FROM data')
    except sqlite3.OperationalError:
        print("\n\n DATABASE DOES NOT EXIST. MADE ONE INSTEAD. \n\n")
        cursor_db.execute('CREATE TABLE "data" (date TEXT NOT NULL,temp INTEGER NOT NULL);')
        search_action = cursor_db.execute('SELECT date, temp FROM data')
    for row in search_action:
        if row[0][:10] == time.ctime()[:10]:
            labels.append(row[0][11:-8])
            graphdata.append(row[1])
    db.close()    
    labels = Markup(labels)
    return render_template('graph.html', graphdata=graphdata, labels=labels)