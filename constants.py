#!/usr/bin/env python3

# Created by: Douglass Jeffrey
# Created on: Oct 2019
# Created on: October 2019
# This program contains constants for circuitpython 6 tutorial

# Circuitpython screen size is 160x120 and sprites are 16x16
SCREEN_X = 160
SCREEN_Y = 120
SCREEN_GRID_X = 16
SCREEN_GRID_Y = 8
SPRITE_SIZE = 16
FPS = 60
NEW_PALETTE = (b'\xff\xff\x00\x22\xcey\x22\xff\xff\xff\xff\xff\xff\xff\xff\xff'
    b'\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff')

# Using for button state
button_state = {
    "button_up": "up",
    "button_just_pressed": "just pressed",
    "button_still_pressed": "still pressed",
    "button_released": "released"
}
