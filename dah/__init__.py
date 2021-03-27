from flask import Flask, render_template, Markup
import time
import sqlite3
import os
from threading import Thread
from dah.views import *
from dah.server import *

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

app = Flask(__name__)
app.secret_key = "92ab7482d48e147f67df277a271fe6d7cdc18321bb2c0268"

def run():
    """Starts running the webapp
    and simultaniously stars running the
    py server that is connected to the 
    ESP32
    """
    record = Thread(target=get_temperature)
    record.setDaemon(True)
    web = Thread(target=app.run)
    record.start()
    web.start()
    

if __name__ == "__main__":
    run()