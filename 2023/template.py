# Add the parent directory to the Python path so `common` can be found
import re
import math
import os
import sys
import functools
import itertools

parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parent_dir)

import common.util as util

DAY = 13
RELATIVE_PATH = f"2023/data/day{DAY:02d}.txt"

def part1(input:str) -> int:
    pass

def part2(input:str) -> int:
    pass

if __name__ == "__main__":
    util.set_debug(False)
    sample = util.read_strs("2023/data/{DAY:02d}-sample.txt")
    input = util.read_strs(RELATIVE_PATH)

    print("PART 1")
    print(part1(input))

    print("PART 2")
    print(part2(input))