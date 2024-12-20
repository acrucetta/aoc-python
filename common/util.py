"""
Utility functions and classes for Advent of Code
"""

import math
import copy
import os
from typing import List, Tuple
import numpy as np
from shapely import Point
import shapely.geometry
import shapely.affinity

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
        print("\x1b[34;1m", end="")  # Set text color to blue
        print(*args, end="")
        print("\x1b[0m")  # Reset text color


def call_and_print(fn, *args):
    """
    Call a function with some parameters, and print the
    function call and the return value.
    """
    str_args = ", ".join(repr(arg) for arg in args)

    if len(str_args) > 20:
        str_args = str_args[:20] + "..."

    print("{}({}) = {}".format(fn.__name__, str_args, fn(*args)))


def print_grid(grid):
    """
    Print a grid.
    """
    rows = ["".join(str(x) for x in row) for row in grid]
    print("\n".join(rows))


#
# FILE I/O
#


def read_strs(filename, sep=None):
    """
    Read strings from a file, separated by whitespace or by the
    specified separator.
    """
    print("Current working dir:", os.getcwd())
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


def parse_grid(strs: str) -> List[List[str]]:
    """
    Parse a string into a grid.
    """
    rows = strs.split("\n")
    grid = [list(row) for row in rows]
    return grid


#
# GRID
#

Grid = List[List[int | str]]


def in_bounds(point: Tuple[int, int], grid: Grid):
    row, col = point
    max_row, max_col = len(grid) - 1, len(grid[0]) - 1
    if 0 <= row <= max_row and 0 <= col <= max_col:
        return True
    return False


#
# DIRECTIONS
#

CARDINAL_DIRECTIONS = [(0, -1), (0, 1), (-1, 0), (1, 0)]


class Direction:
    def __init__(self, row, col):
        self.row = row
        self.col = col

    def to_tuple(self):
        return (self.row, self.col)

    @classmethod
    def UP(cls):
        return cls(-1, 0)

    @classmethod
    def DOWN(cls):
        return cls(1, 0)

    @classmethod
    def LEFT(cls):
        return cls(0, -1)

    @classmethod
    def RIGHT(cls):
        return cls(0, 1)

    