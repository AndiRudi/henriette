from lib import lcddriver
import Adafruit_PCA9685 #ServoDriver https://github.com/adafruit/Adafruit_Python_PCA9685
import netifaces
import json
from collections import deque
from datetime import datetime
from time import *
from flask import Flask, url_for, jsonify, render_template, request 

# Globals
app = Flask(__name__, 
            static_url_path='', 
            static_folder='client/static',
            template_folder='client/templates')

thrust = 0
rudder = 0
servo_min = 150  # Min pulse length out of 4096
servo_max = 600 # Max pulse length out of 4096

try:
    pwm = Adafruit_PCA9685.PCA9685()
except:
    print("Could not initialize pwm")


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
    
    if (thrust > 100):
        thrust = 100
    
    if (thrust < 0):
        thrust = 0

    servo_range = servo_max - servo_min
    servo_step = servo_range / 100
    servo_steps = thrust * servo_step
    amount = servo_min + servo_steps
    print("Thrust: Range: " + str(servo_range))
    print("Thrust: Step: "  + str(servo_step))
    print("Thrust: Steps: " + str(servo_steps))
    print("Thrust: Amount: " + str(amount))

    set_servo_pulse(0, amount) 
   
    writeDebug("Thrust: " + str(thrust) + "%")

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
        print(text)
    except:
        print(text)


def set_servo_pulse(channel, pulse):
    pulse_length = 1000000    # 1,000,000 us per second
    pulse_length //= 60       # 60 Hz
    print('{0}us per period'.format(pulse_length))
    pulse_length //= 4096     # 12 bits of resolution
    print('{0}us per bit'.format(pulse_length))
    pulse *= 1000
    pulse //= pulse_length
    pwm.set_pwm(channel, 0, pulse)

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

# Initalize servo and reset
writeDebug("Initializing servo motors")
pwm.set_pwm_freq(60)
writeDebug("Resetting servo")
set_servo_pulse(0, servo_min) 
set_servo_pulse(1, servo_min) 
writeDebug("Completed initializing servos")
