# Add the parent directory to the Python path so `common` can be found
import re
import math
import os
import sys
import functools
import itertools
import numpy as np
import numpy.typing as npt

parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parent_dir)

import common.util as util

os.chdir(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

DAY = 14
MAIN_PATH = f"2023/data/day{DAY:02d}.txt"
SAMPLE_PATH = f"2023/data/day{DAY:02d}-sample.txt"

"""
DAY 14:

We have a grid of round rocks, cube-shaped rocks, and empty spaces.
When we tilt the platform north, we want to find the new
location of the round rocks. 

Finally we will calculate the total load by adding up the
individual weights of the round rocks. The load of a single
rounded rock is equal to the # of rows from the rock to the south 
edge of the platform; including the current row.

Caveats:
- The round rocks will roll until they hit a cube-shaped rock or 
    the edge of the platform.
- The cube-shaped rocks will not move.

Approach:
- Iterate over each column in the grid.
- Build a new grid with the same dimensions as the original.
- As we iterate over each row, we will keep a tally of the last
empty space; if we encounter a round rock, we will move it to the
last empty space in the new grid.
- If we encounter a cube-shaped rock, we will leave it in place in
the new grid.
- If we encounter an empty space, we will leave it in place in the
new grid; it can be overwritten by a round rock later.
"""


def calculate_load(grid: npt.NDArray[np.character]) -> int:
    max_x, _ = grid.shape
    total_load = 0
    for row in range(max_x):
        rounded_rocks = list(np.where(grid[row] == "O")[0])
        total_load += len(rounded_rocks) * (max_x - row)
    return total_load

def cycle(grid: npt.NDArray[np.character]) -> npt.NDArray[np.character]:
    for _ in range(4):
        grid = tilt(grid)
        grid = np.rot90(grid)
    return grid

# def run_cycles(grid: npt.NDArray[np.character], cycles: int) -> int:
#     load : int = 0
#     for _ in range(cycles):
#         grid = cycle(grid)
#         load = calculate_load(grid)
#     return load

def run_cycles(grid: npt.NDArray[np.character], cycles: int) -> int:
    cache = {}
    load = 0
    cycle_num = 0

    while cycle_num < cycles:
        # Convert grid to a hashable form
        grid_key = tuple(map(tuple, grid))

        if grid_key in cache:
            prev_cycle, prev_load = cache[grid_key]
            cycle_length = cycle_num - prev_cycle

            # Calculate how many full cycles we can skip
            remaining_cycles = cycles - cycle_num
            full_cycles_to_skip = remaining_cycles // cycle_length

            cycle_num += full_cycles_to_skip * cycle_length
            load = prev_load
            continue

        # Cache the current state
        cache[grid_key] = (cycle_num, load)

        # Perform the cycle
        grid = cycle(grid)
        load = calculate_load(grid)
        cycle_num += 1

    return load

def tilt(grid: npt.NDArray[np.character]) -> npt.NDArray[np.character]:
    max_x, max_y = grid.shape
    # Iterate over each column
    for col in range(max_y):
        first_empty = -1

        for row in range(max_x):
            spot = grid[row][col]

            # If we encounter a cube-shaped rock, leave it in place
            if spot == "#":
                first_empty = -1
            elif spot == "." and first_empty == -1:
                first_empty = row
            # If we encounter a round rock, move it to the last empty space
            elif spot == "O":
                if first_empty != -1:
                    grid[first_empty][col] = "O"
                    grid[row][col] = "."
                    first_empty += 1
    return grid


def part1(grid: npt.NDArray[np.character]) -> int:
    north_tilt = tilt(grid)
    return calculate_load(north_tilt)


def part2(grid: npt.NDArray[np.character]) -> int:
    return run_cycles(grid, 1000000001)


if __name__ == "__main__":
    util.set_debug(False)
    input = util.read_str_grid(MAIN_PATH)
    sample = util.read_str_grid(SAMPLE_PATH)

    # print(sample)
    print("PART 1")
    # print(part1(input))
    print(part1(sample))

    print("PART 2")
    # print(part2(input))
    print(part2(sample))
