#import lcddriver
import netifaces
import json
from collections import deque
from datetime import datetime
from time import *
from flask import Flask, url_for, jsonify, render_template, request 

app = Flask(__name__, 
            static_url_path='', 
            static_folder='www/static',
            template_folder='www/templates')

thrust = 0
rudder = 0

@app.route('/')
def api_root():
    return render_template("index.html", title = 'Henriette')

@app.route('/overview')
def api_overview():
    data = {
        'thrust' : thrust,
        'rudder' : rudder
    }

    return jsonify(data)

@app.route('/thrust', methods=['POST'])
def api_thrust():

    thrust = request.json['amount']
    writeDebug("Thrust: " + str(thrust))

    data = {
        'thrust' : thrust,
        'rudder' : rudder
    }

    return jsonify(data)

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
    try:
        global lcdView
        lcdView.popleft()
        lcdView.append(text)
        lcd.lcd_display_string(lcdView[0], 1)
        lcd.lcd_display_string(lcdView[1], 2)
        lcd.lcd_display_string(lcdView[2], 3)
        lcd.lcd_display_string(lcdView[3], 4)
    except:
        print(text)


# Main Application
try:
    lcdView = deque(['', '', '', ''])
    lcd = lcddriver.lcd()
    lcd.lcd_clear()
    writeDebug("henOS starting up")
    writeDebug(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
except:
    print("Could not access display")

# Use netifaces to get the IP
try:
    addrs = netifaces.ifaddresses('wlan0')
    writeDebug("wlan0:" + str(addrs[netifaces.AF_INET][0]["addr"]))
except:
    print("Could not access wlan interface")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int("80"), debug=True)
