import colorsys
from random import random
import time

from openrazer.client import DeviceManager
from pynput import mouse

import threading

razer_device_manager = DeviceManager()

for device in razer_device_manager.devices:
    if device.type == "mousemat":
        firefly = device
    if device.type == "mouse":
        adder = device

if not firefly:
    raise Exception("Could not find firefly!")
if not adder:
    raise Exception("Could not find death adder!")


def react(x, y, button, down):
    #print(x, y, button, down)

    # Don't change color on button release
    if down:
        color = list(map(lambda x: int(x * 255), colorsys.hsv_to_rgb(random(), 1, 1)))
        threading.Thread(target=fade_firefly, args=('both', color)).start()
        threading.Thread(target=fade_adder, args=('logo', color)).start()
        threading.Thread(target=fade_adder, args=('scroll_wheel', color)).start()

def onscroll(x, y, dx, dy):
    #print(x, y, dx, dy)

    color =  list(map(lambda x: int(x * 255), colorsys.hsv_to_rgb(random(), 1, 1)))
    if dy > 0:
        threading.Thread(target=fade_firefly, args=('left', color)).start()
        threading.Thread(target=fade_adder, args=('scroll_wheel', color)).start()
    elif dy < 0:
        threading.Thread(target=fade_firefly, args=('right', color)).start()
        threading.Thread(target=fade_adder, args=('logo', color)).start()

def fade_adder(side, color):
    #print('Fading adder: {}, {}'.format(side, color))
    adder.fx.none()
    maxColor = 1
    fade = 5
    cols = adder.fx.advanced.cols
    row = 0
    while maxColor > 0:
        newMax = 0
        for col in color:
            if col > newMax:
                newMax = col
        maxColor = newMax
        if side == 'logo':
            for col in range(cols):
                if col <= (cols-1)/2.0:
                    adder.fx.advanced.matrix[row, col] = [0,0,0]
                    continue
                adder.fx.advanced.matrix[row, col] = color
        elif side == 'scroll_wheel':
            for col in range(cols):
                if col > (cols-1)/2.0:
                    adder.fx.advanced.matrix[row, col] = [0,0,0]
                    continue
                adder.fx.advanced.matrix[row, col] = color
        adder.fx.advanced.draw()
        for i in range(len(color)):
            if color[i] - fade > 0:
                color[i] -= fade
            else:
                color[i] = 0

def fade_firefly(side, color):
    adder.fx.none()
    maxColor = 1
    fade = 5
    cols = firefly.fx.advanced.cols
    row = 0
    while maxColor > 0:
        newMax = 0
        for col in color:
            if col > newMax:
                newMax = col
        maxColor = newMax
        if side == 'left':
            for col in range(cols):
                if col < cols/2:
                    firefly.fx.advanced.matrix[row, col] = [0,0,0]
                    continue
                firefly.fx.advanced.matrix[row, col] = color
            firefly.fx.advanced.draw()
        elif side == 'right':
            for col in range(cols):
                if col > cols/2:
                    firefly.fx.advanced.matrix[row, col] = [0,0,0]
                    continue
                firefly.fx.advanced.matrix[row, col] = color
            firefly.fx.advanced.draw()
        elif side == 'both':
            for col in range(cols):
                firefly.fx.advanced.matrix[row, col] = color
            firefly.fx.advanced.draw()
        for i in range(len(color)):
            if color[i] - fade > 0:
                color[i] -= fade
            else:
                color[i] = 0

while True:
    try:
        with mouse.Listener(on_click=react, on_scroll=onscroll) as mouse_listener:
            mouse_listener.join()
    except Exception as e:
        print(e)
