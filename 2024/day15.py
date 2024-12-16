# Add the parent directory to the Python path so `common` can be found
import re
import math
import os
import sys
import functools
import itertools
from typing import List, Tuple
import util as util

"""
Steps:
- Parse the input into:
    - A grid
    - A list of directions
- Move the "@" in the grid,  add behavior to account for it.

##########
#..O..O.O#
#......O.#
#.OO..O.O#
#..O@..O.#
#O#..O...#
#O..O..O.#
#.OO.O.OO#
#....O...#
##########

<vv>^<v^>v>^vv^v>v<>v^v<v<^vv<<<^><<><>>v<vvv<>^v^>^<<<><<v<<<v^vv^v>^
"""

DAY = 15
MAIN_PATH = f"2024/data/day{DAY:02d}.txt"
SAMPLE_PATH = f"2024/samples/day{DAY:02d}.txt"


def parse_moves(moves: str) -> List[util.Direction]:
    """Parse: <vv>^<v^> to a list of directions"""
    dirs = []
    for ch in moves:
        match ch:
            case "^":
                dirs.append(util.Direction.UP())
            case "v":
                dirs.append(util.Direction.DOWN())
            case "<":
                dirs.append(util.Direction.LEFT())
            case ">":
                dirs.append(util.Direction.RIGHT())
            case "\n":
                continue
    return dirs


class Grid:
    def __init__(self, grid: List[List[str]]) -> None:
        self.max_row = len(grid)
        self.max_col = len(grid[0])
        self.grid = grid
        self.robot = (-1, -1)
        for row, row_vals in enumerate(self.grid):
            for col, val in enumerate(row_vals):
                if val == "@":
                    self.robot = (row, col)

    def widen_grid(self):
        """
        To get the wider warehouse's map, start with your original map and,
        for each tile, make the following changes:
        - If the tile is #, the new map contains ## instead.
        - If the tile is O, the new map contains [] instead.
        - If the tile is ., the new map contains .. instead.
        - If the tile is @, the new map contains @. instead.
        This will produce a new warehouse map which is twice as wide and with wid
        """
        for row, row_vals in enumerate(self.grid):
            for col, val in enumerate(row_vals):
                if val == "#":
                    self.grid[row][col] = "##"
                elif val == "O":
                    self.grid[row][col] = "[]"
                elif val == ".":
                    self.grid[row][col] = ".."
                elif val == "@":
                    self.grid[row][col] = "@."

    def in_bounds(self, point: Tuple[int, int]):
        row, col = point
        if 0 <= row <= self.max_row and 0 <= col <= self.max_col:
            return True
        return False

    def _move_objects(self, obj: Tuple[int, int], direction: Tuple[int, int]):
        dr, dc = direction
        r, c = obj
        nr, nc = r + dr, c + dc
        if not self.in_bounds((nr, nc)):
            return

        next_cell = self.grid[nr][nc]
        if next_cell == "#":
            # We can't move the object past the current cell
            return
        elif next_cell == ".":
            # We can move the object with no impediments
            self.grid[nr][nc] = "O"
            self.grid[r][c] = "."
        elif next_cell == "O":
            # We have an object on the way, move that
            # object too
            self._move_objects((nr, nc), direction)
            if self.grid[nr][nc] == ".":
                self.grid[nr][nc] = "O"
                self.grid[r][c] = "."

    def move_robot(self, direction: util.Direction):
        """
        Move robot to new point and move anything in the way.

        Case 1: Nothing in the way, move as usual.
        Case 2: Object on the way, move object and anything
        ahead of it, until we hit the wall.
        Case 3: Moving into a wall, remain in place.
        """
        dr, dc = direction.to_tuple()
        r, c = self.robot
        nr, nc = r + dr, c + dc
        if self.in_bounds((nr, nc)):
            next_cell = self.grid[nr][nc]
            if next_cell == ".":
                # Move to the next location
                self.robot = (nr, nc)
                self.grid[r][c] = "."
                self.grid[nr][nc] = "@"
            elif next_cell == "#":
                # Remain in place
                self.robot = (r, c)
            elif next_cell == "O":
                self._move_objects((nr, nc), (dr, dc))

    def __str__(self):
        grid_str = "\n".join("".join(row) for row in self.grid)
        return f"{grid_str}"


def part1(input: str) -> int:
    grid = Grid(util.parse_grid(input[0]))
    moves = parse_moves(input[1])
    print("Initial state:\n\n", grid)
    for i, move in enumerate(moves[:5]):
        print(f"Move #: {i}; {move.to_tuple()}")
        grid.move_robot(move)
        print(grid)


def part2(input: str) -> int:
    grid = Grid(util.parse_grid(input[0]))
    moves = parse_moves(input[1])
    grid.widen_grid()
    print("Initial state:\n\n", grid)
    for i, move in enumerate(moves[:5]):
        print(f"Move #: {i}; {move.to_tuple()}")
        grid.move_robot(move)
        print(grid)


if __name__ == "__main__":
    util.set_debug(False)
    input = util.read_strs(MAIN_PATH, "\n\n")
    sample = util.read_strs(SAMPLE_PATH, "\n\n")

    print("PART 1")
    # util.call_and_print(part1, input)
    # util.call_and_print(part1, sample)

    print("PART 2")
    # part2(input)
    util.call_and_print(part2, input)
    # util.call_and_print(part2, sample)
