#!/usr/bin/env python

import keyboard

def loop():
    while True:
        key = keyboard.read_key()
        print(key)
        if key == "space":
            print("You pressed space")
        if key == "esc":
            break

def destroy():   # When "Ctrl+C" is pressed, the function is executed.
    print("end")

if __name__ == '__main__':  # Program starting from here
    try:
        loop()
    except KeyboardInterrupt:
        destroy()