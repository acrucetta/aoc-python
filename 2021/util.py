"""
Utility functions and classes for Advent of Code
"""

import shapely.geometry
import shapely.affinity
import math
import copy
import parse

#
# DEBUGGING/LOGGING
#

DEBUG=False

def set_debug(debug):
    """
    Enables/disables debug messages
    """
    global DEBUG
    DEBUG = debug


def log(*args):
    """
    Prints a debugging message (if debugging messages are enabled)
    """
    if DEBUG: 
        print('\x1b[7;30;47m', end="")
        print(*args, end="")
        print('\x1b[0m')
        
def call_and_print(fn, *args):
    """
    Call a function with some parameters, and print the
    function call and the return value.
    """
    str_args = ", ".join(repr(arg) for arg in args)

    if len(str_args) > 20:
        str_args = str_args[:20] + "..."

    print("{}({}) = {}".format(fn.__name__, str_args, fn(*args)))


#
# FILE I/O
#

def read_strs(filename, sep=None):
    """
    Read strings from a file, separated by whitespace or by the
    specified separator.
    """
    with open(filename) as f:
        txt = f.read().strip()
        strs = txt.split(sep=sep)    

    return strs


