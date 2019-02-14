#!/usr/bin/python

from Adafruit_PWM_Servo_Driver import PWM
import time
import argparse

# ===========================================================================
# Example Code
# ===========================================================================

# Initialise the PWM device using the default address
#pwm = PWM(0x40)
# Note if you'd like more debug output you can instead run:
pwm = PWM(0x40, debug=True)

servoMin = 160  # Min pulse length out of 4096
servoMax = 320  # Max pulse length out of 4096

def setServoPulse(channel, pulse):
  pulseLength = 1000000                   # 1,000,000 us per second
  pulseLength /= 60                       # 60 Hz
  print "%d us per period" % pulseLength
  pulseLength /= 4096                     # 12 bits of resolution
  print "%d us per bit" % pulseLength
  pulse *= 1000
  pulse /= pulseLength
  pwm.setPWM(channel, 0, pulse)

def loop():
  runLoop = True
  servo0 = 0
  servo1 = 0 
  while runLoop:
    key = raw_input('Enter key')
    
    if key == 'q': 
      runLoop = false

    if key == 'a':
      servo1 +=10

    if key == 'd':
      servo1 -=10

    pwm.setPWM(1, 0, servo1)


parser = argparse.ArgumentParser()
parser.add_argument("-s", "--servo", help="Set the servo", type=int, choices=[0, 1])
parser.add_argument("-p", "--pulse", help="Set the puls", type=int)
parser.add_argument("-l", "--loop", help="Go into loop mode")
args = parser.parse_args()

pwm.setPWMFreq(60)                        # Set frequency to 60 Hz

if args.loop:
  loop()
else:
  print "Setting servo {} to {}".format(args.servo, args.pulse)
  pwm.setPWM(args.servo, 0, args.pulse)




