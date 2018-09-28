#!/usr/bin/python3

import colorsys
from random import random
from math import floor
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

color = [0, 255, 0]
max_paths = 6
cur_paths = 0
paths = []

class Path:
    def __init__(self, rows, cols):
        # Todo
        self.y = 0
        self.x = floor(random() * cols)
        self.length = floor(random() * rows)
        self.rows = rows
        self.cols = cols
        self.alive = True

    def update(self):
        # Todo
        self.y += 1
        if self.y - self.length > self.rows:
            self.alive = False
            return False
        return True

    def draw(self):
        # Todo
        if not self.alive:
            return
        max_y = self.rows
        if self.y < self.rows:
            max_y = self.y
        cur_y = 0
        if self.y - self.length > 0:
            cur_y = self.y - self.length
        for y in range(cur_y, max_y):
            keyboard.fx.advanced.matrix[y, self.x] = color

def clear(device):
    for row in range(device.fx.advanced.rows):
        for col in range(device.fx.advanced.cols):
            device.fx.advanced.matrix[row, col] = [0, 0, 0]
    device.fx.advanced.draw()

while True:
    clear(keyboard)
    if cur_paths < max_paths:
        paths.append(Path(rows, cols))
    for path in paths:
        if path.alive:
            if not  path.update():
                cur_paths -= 1
            path.draw()
    keyboard.fx.advanced.draw()
    time.sleep(0.5)
