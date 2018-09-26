#!/usr/bin/python3
from pynput import mouse
import os

def react(x, y, button, down):
    print(x, y, button, down)
    if str(button) == 'Button.button9' and down:
        print("reacting")
        os.system("/usr/bin/xte 'keydown Control_L' 'keydown Tab' 'keyup Tab' 'keyup Control_L'")
    elif str(button) == 'Button.button8' and down:
        print("reacting")
        os.system("/usr/bin/xte 'keydown Control_L' 'keydown Shift_L' 'keydown Tab' 'keyup Tab' 'keyup Shift_L' 'keyup Control_L'")

while True:
    try:
        with mouse.Listener(on_click=react) as mouse_listener:
            mouse_listener.join()
    except Exception as e:
        print(e)
