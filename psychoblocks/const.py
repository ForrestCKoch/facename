# -*- coding: utf-8 -*-
###############################################################################
# Written by:       Forrest Koch (forrest.koch@unsw.edu.au)
# Organization:     Centre for Healthy Brain Ageing (UNSW)
# PyschoPy Version: 1.85.3
# Python Version:   2.7.5
###############################################################################
"""
This module contains the magic numbers used throught the facename project
"""

TLL_PULSE   = 84
"""
int: The byte code for the TLL pulse sent from the scanner
"""

RIGHT_INDEX   = 99
"""
int: The byte code for the right index button
"""

RIGHT_MIDDLE  = 100
"""
int: The byte code for the right middle button
"""

LEFT_INDEX    = 98
"""
int: The byte code for the left index button
"""

LEFT_MIDDLE   = 97
"""
int: The byte code for the left middle button
"""

TARGET = 'target'
"""
str: The string used to represent a target stimulus
"""

MISS = 'miss'
"""
str: The string used to represet a non-target stimulus
"""

STIMULI_PATH = 'stimuli'
"""
str: path to the stimuli folder
"""

DEFAULT_PARTICIPANT = 'test'
"""
str: default participant value
"""

DEFAULT_SESSION = '001'
"""
str: default session number
"""

DEFAULT_RUN_FILE = 'run1.csv'
"""
str: default run
"""

DEFAULT_MODE = 'serial'
"""
str: default mode
"""

DEFAULT_PORT = '/dev/ttyACM0'
"""
str: default port for serial device
"""

DEFAULT_BAUDRATE = '57600'
"""
str: default baudrate for serial device
""" 

DEFAULT_FULLSCREEN = 'true'
"""
str: default fullscreen status
"""

DEFAULT_SCREEN_WIDTH = '1024'
"""
str: default screen width
"""

DEFAULT_SCREEN_HEIGHT = '768'
"""
str: default screen height
"""

DEFAULT_STIMULI_FOLDER = 'stimuli'
"""
str: default stimuli folder
"""

DEFAULT_RESULTS_FOLDER = 'data'
"""
str: default results folder
"""

DEFAULT_FONT = 'Arial'
