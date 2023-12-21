"""
Utility functions and classes for Advent of Code
"""

import math
import copy
from typing import Tuple
import numpy as np
import shapely.geometry
import shapely.affinity

# References:
# github.com/borja

#
# DEBUGGING/LOGGING
#

DEBUG = False


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
        print("\x1b[7;30;47m", end="")
        print(*args, end="")
        print("\x1b[0m")


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


def read_grid(filepath):
    """
    Reads matrix from the filepath.
    """
    with open(filepath) as f:
        data = f.readlines()

    rows = list(map(lambda x: x.strip("\n"), data))
    matrix = []

    for row in rows:
        split_row = [int(r) for r in row]
        matrix.append(split_row)

    return np.array(matrix)


def read_str_grid(filepath):
    """
    Reads matrix from the filepath.
    """
    with open(filepath) as f:
        data = f.readlines()

    rows = list(map(lambda x: x.strip("\n"), data))
    matrix = []

    for row in rows:
        split_row = [r for r in row]
        matrix.append(split_row)

    return matrix


def parse_grid(strs: str) -> list[list[str]]:
    """
    Parse a string into a grid.
    """
    rows = strs.split("\n")
    grid = [list(row) for row in rows]
    return grid


#
# DIRECTIONS
#


class Direction:
    def __init__(self, x, y):
        self._p = shapely.geometry.Point(x, y)

    @classmethod
    def UP(cls):
        return cls(0, -1)

    @classmethod
    def DOWN(cls):
        return cls(0, 1)

    @classmethod
    def LEFT(cls):
        return cls(-1, 0)

    @classmethod
    def RIGHT(cls):
        return cls(1, 0)

    def __eq__(self, other):
        # return self._p.x == other._p.x and self._p.y == other._p.y
        return self._p == other._p

    def __hash__(self):
        # return hash((self._p.x, self._p.y))
        return hash(self._p)

    def __copy__(self):
        return Direction(self._p.x, self._p.y)

    def __repr__(self) -> str:
        return f"<{self._p.x}, {self._p.y}>"


