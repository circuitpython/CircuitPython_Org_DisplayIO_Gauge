# SPDX-FileCopyrightText: Copyright (c) 2021 GaryZ
#
# SPDX-License-Identifier: Unlicense

"""
Create multiple gauge's and change their level.
This works on any CircuitPython device with a built-in display.
"""


import time
import board
import displayio
from displayio_gauge import Gauge

display = board.DISPLAY

# Make the display context
main_group = displayio.Group()

# Make a background color fill
color_bitmap = displayio.Bitmap(display.width, display.height, 1)
color_palette = displayio.Palette(1)
color_palette[0] = 0x000000
bg_sprite = displayio.TileGrid(color_bitmap, pixel_shader=color_palette, x=0, y=0)
main_group.append(bg_sprite)
display.show(main_group)


gauge1 = Gauge(
    x=30,
    y=30,
    radius=27,
    thickness=3,
    level=10,
    outline_color=0xFFFFFF,
    foreground_color=0x00FF00,
    background_color=0x000000,
)
main_group.append(gauge1)

gauge2 = Gauge(
    x=90,
    y=30,
    radius=27,
    thickness=8,
    level=30,
    outline_color=0xFFFFFF,
    foreground_color=0x00FF00,
    background_color=0x000000,
)
main_group.append(gauge2)
gauge3 = Gauge(
    x=150,
    y=30,
    radius=27,
    thickness=10,
    level=60,
    outline_color=0xFFFFFF,
    foreground_color=0xFF0000,
    background_color=0x000000,
)
main_group.append(gauge3)

gauge4 = Gauge(
    x=210,
    y=30,
    radius=28,
    thickness=12,
    level=0,
    outline_color=0xFFFFFF,
    foreground_color=0xFF0000,
    background_color=0x000000,
)
main_group.append(gauge4)


gauge5 = Gauge(
    x=120,
    y=120,
    radius=50,
    thickness=20,
    level=0,
    outline_color=0xFFFFFF,
    foreground_color=0x00FF00,
    background_color=0x000000,
)
main_group.append(gauge5)

while True:

    for i in range(0, 101, 4):
        if i >= 80:
            gauge4.foreground_color = 0xFF0000
            gauge5.foreground_color = 0xFF0000
        else:
            gauge4.foreground_color = 0x00FF00
            gauge5.foreground_color = 0x00FF00

        gauge4.level= i
        gauge5.level = i
        time.sleep(0.1)

    for i in range(100, 0, -4):
        if i >= 80:
            gauge4.foreground_color = 0xFF0000
            gauge5.foreground_color = 0xFF0000
        else:
            gauge4.foreground_color = 0x00FF00
            gauge5.foreground_color = 0x00FF00

        gauge4.level= i
        gauge5.level = i
        time.sleep(0.1)
