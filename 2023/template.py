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

os.chdir(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

DAY = 00
MAIN_PATH = f"2023/data/day{DAY:02d}.txt"
SAMPLE_PATH = "2023/data/day{DAY:02d}-sample.txt")

def part1(input:str) -> int:
    pass

def part2(input:str) -> int:
    pass

if __name__ == "__main__":
    util.set_debug(False)
    input = util.read_strs(MAIN_PATH, sep="\n")
    sample = util.read_strs(SAMPLE_PATH, sep="\n")

    print("PART 1")
    # part1(input)
    part1(sample)

    print("PART 2")
    # part2(input)
    # part2(sample)