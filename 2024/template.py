# Add the parent directory to the Python path so `common` can be found
import re
import math
import os
import sys
import functools
import itertools
import util as util

DAY = 12
MAIN_PATH = f"2024/data/day{DAY:02d}.txt"
SAMPLE_PATH = f"2024/samples/day{DAY:02d}.txt"

def part1(input:str) -> int:
    pass

def part2(input:str) -> int:
    pass

if __name__ == "__main__":
    util.set_debug(False)
    input = util.read_strs(MAIN_PATH)
    sample = util.read_strs(SAMPLE_PATH)

    print("PART 1")
    # util.call_and_print(part1, input)
    # util.call_and_print(part1, sample)

    print("PART 2")
    # part2(input)
    util.call_and_print(part2, input)
    # util.call_and_print(part2, sample)
