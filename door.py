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
    open_position = 400

    def __init__(self, channel):
        self.channel = channel
        pwm.setPWM(self.channel, 0, self.closed_position)

    def open(self):
        print "Opening door"
        for i in xrange(self.closed_position, self.open_position, 5):
            pwm.setPWM(self.channel, 0, i)
            time.sleep(.1)

    def close(self):
        print "Closing door"
        for i in xrange(self.open_position, self.closed_position, -5):
            pwm.setPWM(self.channel, 0, i)
            time.sleep(.1)

class GarageDoor(Door):
    closed_position = 150
    open_position = 400

if __name__ == "__main__":
    for d in (Door(0), GarageDoor(3)):
        d.open()
        d.close()

