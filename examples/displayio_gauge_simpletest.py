# SPDX-FileCopyrightText: Copyright (c) 2021 Tim Cocks
#
# SPDX-License-Identifier: Unlicense

"""
Create a single gauge and change it's level
This works on any CircuitPython device with a built-in display.
"""

import time
import board
import displayio
from displayio_gauge import Gauge

display = board.DISPLAY

# Make the display context
main_group = displayio.Group()

color_bitmap = displayio.Bitmap(display.width, display.height, 1)
color_palette = displayio.Palette(1)
color_palette[0] = 0x000000
bg_sprite = displayio.TileGrid(color_bitmap, pixel_shader=color_palette, x=0, y=0)
main_group.append(bg_sprite)

display.show(main_group)


example_gauge = Gauge(
    x=35,
    y=35,
    radius=30,
    foreground_color=0x00FF00,
    background_color=0x000000,
    outline_color=0xFFFFFF,
)
main_group.append(example_gauge)

while True:
    for i in range(0, 101):
        example_gauge.level = i
        time.sleep(0.05)
