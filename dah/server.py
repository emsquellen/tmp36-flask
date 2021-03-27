from flask import Flask, render_template, Markup
import time
import sqlite3
import os
import socket
from dah import app
from sys import exit
import configparser
config = configparser.ConfigParser()
config.read('config.ini')
ip = config['Settings']['ip address']

import ipaddress
try:
    addr = ipaddress.IPv4Address(ip)
except ValueError:
    print('IP address invalid.')
    exit(-1)
if addr.is_global:
    print('IP address invalid.')
    exit(-1)
elif addr.is_private:
    pass



led = False

@app.route('/led')
def led():
    global led
    led = False if led else True

def get_temperature():
    HOST = ip
    PORT = 4000
    ALLOKA = "OK_A"
    ALLOKB = "OK_B"
    ALARMA = "LIGHT_ON_A"
    ALARMB = "LIGHT_ON_B"
    global led
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        print("Binding done, waiting for client")
        s.listen()
        conn, addr = s.accept()
        with conn:
            
            print("Connected by", addr)
            db = sqlite3.connect("temp.db", detect_types=sqlite3.PARSE_DECLTYPES)
            cursor_db = db.cursor()
            while True:
                data = conn.recv(1024)
                message = data.decode("utf-8")
                print("Received data: ", message)
                if not data:
                    break
                try:
                    cursor_db.execute(f"INSERT INTO data VALUES ('{time.ctime()}', {int(message)});")
                except sqlite3.OperationalError:
                    print("\n\n DATABASE DOES NOT EXIST. MADE ONE INSTEAD. \n\n")
                    cursor_db.execute('CREATE TABLE "data" (date TEXT NOT NULL,temp INTEGER NOT NULL);')
                    cursor_db.execute(f"INSERT INTO data VALUES ('{time.ctime()}', {int(message)});")
                db.commit()
                if not led:
                    if int(data) <= 21:
                        conn.send(ALLOKA.encode("utf-8"))
                        print(ALLOKA, "sent")
                    else:
                        conn.send(ALARMA.encode("utf-8"))
                        print(ALARMA, "sent")
                if led:
                    if int(data) <= 21:
                        conn.send(ALLOKB.encode("utf-8"))
                        print(ALLOKB, "sent")
                    else:
                        conn.send(ALARMB.encode("utf-8"))
                        print(ALARMB, "sent")

                time.sleep(1)
            db.close()

