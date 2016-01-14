#!/usr/bin/env python
from flask import Flask, render_template, Response

import door

app = Flask(__name__)

doors = [door.GarageDoor(0)]

@app.route('/door/<door>/open')
def open_door(door):
    print "Open %s" % door
    doors[door].open()
    return "OK"

@app.route('/door/<door>/close')
def close_door(door):
    print "Close %s" % door
    doors[door].close()
    return "OK"

if __name__ == '__main__':
    app.run(host='0.0.0.0') #, debug=True)

