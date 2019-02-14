import RPi.GPIO as io
io.setmode(io.BCM)
 
in1_pin = 4
in2_pin = 7
pwm_pin = 8
 
io.setup(in1_pin, io.OUT)
io.setup(in2_pin, io.OUT)
io.setup(pwm_pin, io.OUT)
 
# PWM konfigurieren
# Pulse Weite
motor = io.PWM(pwm_pin, 100)
# Start des Pulses
motor.start(0)
# Stillstand vorgeben
motor.ChangeDutyCycle(0)
 
def geschwindigkeit(speed):
    # Hier wird die Geschwindigkeit geregelt, durch den Multiplikator 11
    # wird eine maximale Pulse Weite von 99 erreicht. In diesem Skript
    # ist eine Pulsweite von 0-100 vorgegeben. 99 ist hierbei das schnellste
    speed = int(speed) * 11
    motor.ChangeDutyCycle(speed)
 
# Die Definition der Richtung ist nicht vorgegeben, da die Pins keine bestimmte
# Belegung voraussetzten.
# Stehen beide Outputs auf False, werden die Motoren blockiert und somit gebremst.
def clockwise():
    io.output(in1_pin, True)
    io.output(in2_pin, False)
 
def counter_clockwise():
    io.output(in1_pin, False)
    io.output(in2_pin, True)
 
clockwise()
 
while True:
    cmd = raw_input("Command, f/r 0..9, E.g. f5 :")
    direction = cmd[0]
    if direction == "f":
        clockwise()
    elif direction == "r":
        counter_clockwise()
    elif direction == "x":
        break
    geschwindigkeit(cmd[1])
 
# Cleanup
io.cleanup()
