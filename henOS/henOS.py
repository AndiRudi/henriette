import lcddriver
import netifaces
import json
from collections import deque
from datetime import datetime
from time import *
from flask import Flask, url_for

app = Flask(__name__)


@app.route('/')
def api_root():
    return 'Welcome to henOS'

@app.route('/overview')
def api_overview():
    data = {
        'version'  : '0',
        'thrust' : +1,
        'rudder' : -2,
        'position' : -2,
        'head' : -2,
        'pump' : -2,
        'temperature' : 'undefined',
        'humidity' : 'undefined',
        'video_url' : ''
    }
    js = json.dumps(data)

    resp = Response(js, status=200, mimetype='application/json')

    return resp

@app.route('/thrust', methods=['POST'])
def api_thrust():
    return 'Engaged'

@app.route('/rudder', methods=['POST'])
def api_rudder():
    return 'Ruddered'

@app.route('/position', methods=['POST'])
def api_position():
    return 'Navigating to'

@app.route('/head', methods=['POST'])
def api_head():
    return 'Head moved'

@app.route('/pump', methods=['POST'])
def api_pump():
    return 'Navigating to'

def writeDebug(text):
    global lcdView
    lcdView.popleft()
    lcdView.append(text)
    lcd.lcd_display_string(lcdView[0], 1)
    lcd.lcd_display_string(lcdView[1], 2)
    lcd.lcd_display_string(lcdView[2], 3)
    lcd.lcd_display_string(lcdView[3], 4)


# Main Application
lcdView = deque(['', '', '', ''])
lcd = lcddriver.lcd()
lcd.lcd_clear()
writeDebug("henOS starting up")
writeDebug(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

# Use netifaces to get the IP
addrs = netifaces.ifaddresses('wlan0')
writeDebug("wlan0:" + str(addrs[netifaces.AF_INET][0]["addr"]))


if __name__ == '__main__':
    app.run(host='0.0.0.0')
