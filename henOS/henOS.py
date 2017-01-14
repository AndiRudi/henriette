import lcddriver
import netifaces
import json
from datetime import datetime
from time import *
from flask import Flask, url_for

app = Flask(__name__)

@app.route('/')
def api_root():
    return 'Welcome to henOS'

@app.route('/articles')
def api_articles():
    return 'List of ' + url_for('api_articles')

# Main Application

lcd = lcddriver.lcd()
lcd.lcd_clear()
lcd.lcd_display_string("henOS starting up", 1)
lcd.lcd_display_string(datetime.now().strftime("%Y-%m-%d %H:%M:%S"), 2)


# Use netifaces to get the IP
addrs = netifaces.ifaddresses('wlan0')
lcd.lcd_display_string("wlan0:" + str(addrs[netifaces.AF_INET][0]["addr"]), 3)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
