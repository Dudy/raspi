#!/usr/bin/env python3

import RPi.GPIO as GPIO
from flask import Flask, render_template, request, abort, jsonify

app = Flask(__name__)

farbe = "000000"
# define GPIO pins to use to command the RGB LED
pins = {'Red':17, 'Green':18, 'Blue':27}


def setup():
    global p_R, p_G, p_B
    # Set the GPIO modes to BCM Numbering
    GPIO.setmode(GPIO.BCM)
    # Set all LedPin's mode to output and initial level to High(3.3v)
    for i in pins:
        GPIO.setup(pins[i], GPIO.OUT, initial=GPIO.HIGH)

    # Set all led as pwm channel and frequece to 2KHz
    p_R = GPIO.PWM(pins['Red'], 2000)
    p_G = GPIO.PWM(pins['Green'], 2000)
    p_B = GPIO.PWM(pins['Blue'], 2000)

    # Set all begin with value 0
    p_R.start(0)
    p_G.start(0)
    p_B.start(0)


# Define a MAP function for mapping values.  Like from 0~255 to 0~100
def MAP(x, in_min, in_max, out_min, out_max):
    return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min


# Define a function to set up colors. Input color should be Hexadecimal with red, green and blue values.
def setColor(color):
    # configures the three LEDs' luminance with the given color value.
    # Calculate RGB values from 'color' variable
    R_val = (color & 0xFF0000) >> 16
    G_val = (color & 0x00FF00) >> 8
    B_val = (color & 0x0000FF) >> 0
    # these three lines are used for analyzing the col variables
    # assign the first two values of the hexadecimal to R, the middle two assigned to G
    # assign the last two values to B, please refer to the shift operation of the hexadecimal for details.

    # Map color value from 0~255 to 0~100
    R_val = MAP(R_val, 0, 255, 0, 100)
    G_val = MAP(G_val, 0, 255, 0, 100)
    B_val = MAP(B_val, 0, 255, 0, 100)

    # Change the colors
    # Assign the mapped duty cycle value to the corresponding PWM channel to change the luminance.
    p_R.ChangeDutyCycle(R_val)
    p_G.ChangeDutyCycle(G_val)
    p_B.ChangeDutyCycle(B_val)

    print("color_msg: R_val = %s,    G_val = %s,    B_val = %s" % (R_val, G_val, B_val))

@app.route('/')
def main():
    return render_template('test.html', farbe = farbe)


@app.route('/farbauswahl', methods=['POST'])
def farbauswahl():
    if not request.json or not 'farbe' in request.json:
        abort(400)
    print(request.json)
    print(request.json['farbe'])

    setColor(int(request.json['farbe'], 16))

    return jsonify(success=True), 200


def destroy():
    # Stop all pwm channel
    p_R.stop()
    p_G.stop()
    p_B.stop()
    # Release resource
    GPIO.cleanup()


# If run this script directly, do:
if __name__ == '__main__':
    setup()
    try:
        app.run(debug=True, port=5000, host='0.0.0.0')
    except KeyboardInterrupt:
        destroy()
