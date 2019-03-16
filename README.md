# henriette

Henriette is a remote controlled swan.

## Setup Raspberry Pi

Follow the installation https://learn.adafruit.com/circuitpython-on-raspberrypi-linux/installing-circuitpython-on-raspberry-pi
Install Servokit `pip3 install adafruit-circuitpython-servokit` and test with scripts mentioned in https://circuitpython.readthedocs.io/projects/servokit/en/latest/

## Installation

Clone the repo, then install pip requirements using

`pip install -r requirements.txt`

## henriette operating system (henOS)

henOS is the main server of henriette. Its purpose is to control all the sensors and motors and it providers a rest endpoint to control the swans movement.

### Boot sequence

At startup henOS.py is downloaded from github and automatically started. This ensures that always the newest version is running. The startup sequence is running and displays the main information on the display.

### Display

The HD44780 display shows relevant information inside the swan and is needed for maintenance. On startup it shows the current version of henOS, the battery status, current IP address and network status. This makes it easy to get a direct connection.

### Thrust and Steering

The forward thrust is done by a 6V Motor controlled by a BEC system connected to the PWM driver board. The ship rudder is controlled with a servo also connected to the PWM driver board. The driver board itself is connected with I2C to the raspberry.

### Head

The head movement is controlled by a Fischertechnik motor connected with the help of a L293D driver chip. Its used to turn the swans head left right.

### Camera

The rasperry camera is used to get a picture from the swans viewpoint.

### GPS Positioning

The swan has an built in GPS sensor to get the current position

### Status Lights

The swan has LEDs to the outside to show issues. 

### Console

The console application is used to see the current status and control the machine with ssh.

### REST API

The public rest api exposed is used to control the swan from the outside. 

/console.py



