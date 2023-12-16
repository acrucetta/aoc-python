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


def part1(input: list[str]) -> int:
    sums = 0
    for strs in input:
        print(strs)
        grid = np.array(util.parse_grid(strs))
        max_row, max_col = grid.shape

        match_addr = (None, 0)  # (direction, index)
        # Check for vertical symmetry
        for i in range(1, max_col + 1):
            # We need to account for the fact that the mirror
            # may not be in the middle of the grid
            len_before = i
            len_after = max_col - i
            if len_before > len_after:
                len_after = len_before
            else:
                len_before = len_after
            arr_before = grid[:, :len_before]
            arr_after = grid[:, -len_after:]

            if np.array_equal(arr_before, arr_after):
                print("Match found at index", i)
                match_addr = ("vertical", i)
                break

        # Check for horizontal symmetry
        for i in range(1, max_row + 1):
            rows_before = grid[:i, :]
            rows_after = grid[i:, :]
            if np.array_equal(rows_before, rows_after):
                match_addr = ("horizontal", i)
                break
        
        match match_addr:
            case ("vertical", i):
                sums += i
            case ("horizontal", i):
                sums += 100 * i
            case _:
                print("No match found")
        
        print(10*"-")
    print(sums)
    return sums


def part2(input: list[str]) -> int:
    pass


if __name__ == "__main__":
    util.set_debug(False)
    sample = util.read_strs(f"2023/data/day{DAY:02d}-sample.txt", sep="\n\n")
    data = util.read_strs(RELATIVE_PATH, sep="\n\n")

    print("PART 1")
    # print(part1(input))
    part1(sample)

    print("PART 2")
    print(part2(input))
