#!/usr/bin/python

from Adafruit_PWM_Servo_Driver import PWM
import time

# Initialise the PWM device using the default address
pwm = PWM(0x40)

# Note if you'd like more debug output you can instead run:
#pwm = PWM(0x40, debug=True)

pwm.setPWMFreq(60) # Set frequency to 60 Hz

class Door(object):
    closed_position = 150
    open_position = 600

    def __init__(self, channel):
        self.channel = channel
        pwm.setPWM(self.channel, 0, self.closed_position)

    def open(self):
        for i in xrange(self.closed_position, self.open_position):
            pwm.setPWM(self.channel, 0, i)
            time.sleep(.1)

    def close(self):
        for i in xrange(self.open_position, self.closed_position):
            pwm.setPWM(self.channel, 0, i)
            time.sleep(.1)

class GarageDoor(Door):
    closed_position = 300
    open_position = 500


