from flask import Flask, render_template, Markup
import time
import sqlite3
import os
from threading import Thread

app = Flask(__name__)
app.secret_key = "92ab7482d48e147f67df277a271fe6d7cdc18321bb2c0268"

from dah.views import *
from dah.server import *


def run_time():
    """Really does nothing but
    makes you able to actually
    exit the app.
    Couldn't find a different easy
    way and this works.
    Is it probably bad code? Yes.
    """
    # Wait a split second because the other 2 also
    # output some lines
    time.sleep(0.1)
    # wait for input of some kind
    while True:
        input()


def run():
    """Starts running the webapp
    and simultaniously stars running the
    py server that is connected to the 
    ESP32
    """
    # Main thread
    main = Thread(target=run_time)

    # Starts getting input
    record = Thread(target=get_temperature)
    record.setDaemon(True)

    # Start the webpage
    web = Thread(target=app.run)
    web.setDaemon(True)

    # Start the threads
    main.start()
    record.start()
    web.start()
        
if __name__ == "__main__":
    run()