#!/usr/bin/python3

import colorsys
from random import random
import time

from openrazer.client import DeviceManager

razer_device_manager = DeviceManager()

for device in razer_device_manager.devices:
    if device.type == "keyboard":
        keyboard = device
    else:
        print("Inspecting {}".format(device))

if not keyboard:
    raise Exception("Could not find keyboard!")

rows = keyboard.fx.advanced.rows
cols = keyboard.fx.advanced.cols

print("Rows: {} Cols: {}".format(rows,cols))

hue = 0

while True:
    for row in range(rows):
        for col in range(cols):
            #print("Setting ({},{}) {}".format(row,col, hue))
            color = list(map(lambda x: int(x * 255), colorsys.hsv_to_rgb(hue, 1, 1)))
            keyboard.fx.advanced.matrix[row, col] = color
            keyboard.fx.advanced.draw()
            hue += 0.025
            time.sleep(0.01)
