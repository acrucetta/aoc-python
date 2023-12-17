# Add the parent directory to the Python path so `common` can be found
import re
import math
import os
import sys
import functools
import itertools

import numpy as np

parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parent_dir)

import common.util as util

os.chdir(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

"""
Day 13:

We want to find the reflection within a grid of # and . characters.

E.g.,

123456789
    ><   
#.##..##.
..#.##.#.
##......#
##......#
..#.##.#.
..##..##.
#.#.##.#.
    ><   
123456789

We want to add up the number of columns to the left of each
vertical reflection; and add 100 multiplied by the number 
of rows above each horizontal reflection.

Above we have 5 columns to the left. (5)

Our strategy will be to iterate over each row in the grid,
and find whether the columns before it and the ones after
it are symmetrical.

We need to only select the length of rows before or after it
since the mirror is not necessarily in the middle.

"""

DAY = 13
RELATIVE_PATH = f"2023/data/day{DAY:02d}.txt"


def array_diffs(arr1, arr2):
    """
    Check how many differences there are between two arrays.
    """
    return np.sum(arr1 != arr2)


def part1(input: list[str]) -> int:
    total_sum = 0
    for strs in input:
        grid = np.array(util.parse_grid(strs))
        max_row, max_col = grid.shape

        for i in range(1, max_col):
            col = min(i, max_col - i)
            left = grid[:, i - col : i]
            right = np.fliplr(grid[:, i : col + i])
            if np.array_equal(left, right):
                total_sum += i

        # Check for horizontal symmetry
        for i in range(1, max_row):
            row = min(i, max_row - i)
            up = grid[i - row : i, :]
            down = np.flipud(grid[i : row + i, :])
            if np.array_equal(up, down):
                total_sum += 100 * i
    print(total_sum)
    return total_sum


def part2(input: list[str]) -> int:
    total_sum = 0
    for strs in input:
        grid = np.array(util.parse_grid(strs))
        max_row, max_col = grid.shape

        for i in range(1, max_col):
            col = min(i, max_col - i)
            left = grid[:, i - col : i]
            right = np.fliplr(grid[:, i : col + i])
            if array_diffs(left, right) == 1:
                total_sum += i

        # Check for horizontal symmetry
        for i in range(1, max_row):
            row = min(i, max_row - i)
            up = grid[i - row : i, :]
            down = np.flipud(grid[i : row + i, :])
            if array_diffs(up, down) == 1:
                total_sum += 100 * i
    print(total_sum)
    return total_sum


if __name__ == "__main__":
    util.set_debug(False)
    sample = util.read_strs(f"2023/data/day{DAY:02d}-sample.txt", sep="\n\n")
    data = util.read_strs(RELATIVE_PATH, sep="\n\n")

    print("PART 1")
    part1(data)

    print("PART 2")
    part2(data)
