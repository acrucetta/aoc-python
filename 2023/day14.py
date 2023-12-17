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


def part1(grid: npt.NDArray[np.character]) -> int:
    
    max_x, max_y = grid.shape
    total_load = 0

    # Iterate over each column
    for col in range(max_y):
        first_empty = -1

        for row in range(max_x):
            spot = grid[row][col]
            
            # If we encounter a cube-shaped rock, leave it in place
            if spot == '#':
                first_empty = -1
            elif spot == '.' and first_empty == -1:
                first_empty = row
            # If we encounter a round rock, move it to the last empty space
            elif spot == 'O':
                if first_empty != -1:
                    grid[first_empty][col] = 'O'
                    grid[row][col] = '.'
                    total_load += (max_x - first_empty) + 1
                    first_empty += 1
    print(grid)
    return total_load



def part2(input: str) -> int:
    pass


if __name__ == "__main__":
    util.set_debug(False)
    # input = util.read_strs(MAIN_PATH, sep="\n")
    sample = util.read_str_grid(SAMPLE_PATH)

    print(sample)
    print("PART 1")
    # part1(input)
    print(part1(sample))


    print("PART 2")
    # part2(input)
    # part2(sample)
