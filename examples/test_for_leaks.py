# SPDX-FileCopyrightText: Copyright (c) 2021 Randall Bohn
#
# SPDX-License-Identifier: MIT
"Test displayio_guage.py -- In certain conditions the fill color was leaking out."
import math
import random
import time
from adafruit_funhouse import FunHouse
from displayio_gauge import Gauge

funhouse = FunHouse()
display = funhouse.display
top_group = funhouse.splash
display.show(top_group)

color_pass = 0x009900
color_fail = 0x990000

def make_gauge(radius, thickness):
    return Gauge(x=display.width//2,y=display.height//2,
        radius=radius, thickness=thickness, level=10,
        outline_color=0xEEEEEE,
        foreground_color=0xFFCC00,
        background_color=0x3333FF)

# pylint: disable=W0212
# test access to gauge._bitmap
def check(gauge):
    bitmap = gauge._bitmap
    top_left = (1,1)
    top_right = (bitmap.width-1,1)
    bottom_center = (bitmap.width//2, bitmap.height-1)
    if bitmap[top_left[0],top_left[1]] != 0:
        raise ValueError("leak detected top_left")
    if bitmap[top_right[0], top_right[1]] != 0:
        raise ValueError("leak detected top_right")
    if bitmap[bottom_center[0], bottom_center[1]] != 0:
        raise ValueError("leak detected bottom_center")


def find_leaks(gauge):
    for x in range(360*3.0):
        theta = math.radians(x)
        level = int(abs(math.sin(theta) * 100))
        gauge.level = level
        check(gauge)



for iteration in range(5):
    my_radius = random.randrange(10,90)
    my_thickness = int(min(
        max(my_radius*0.2, my_radius*random.random()),my_radius*0.85))
    print(f"iteration={iteration} radius={my_radius} thickness={my_thickness}")
    my_gauge = make_gauge(my_radius, my_thickness)
    top_group[0] = my_gauge
    try:
        find_leaks(my_gauge)
        my_gauge.background_color=color_pass
        time.sleep(3)
    except ValueError:
        my_gauge.background_color=color_fail
        break

if my_gauge.background_color == color_pass:
    print("PASS!")
else:
    print(f"FAIL: Leak detected in iteration {iteration} level={my_gauge.level}.")

while True:
    time.sleep(1)
