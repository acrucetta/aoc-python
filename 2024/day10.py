from typing import List, Tuple
from dataclasses import dataclass
import util as util
import colorsys as cs
import numpy as np

DAY = 10
MAIN_PATH = f"2024/data/day{DAY:02d}.txt"
SAMPLE_PATH = f"2024/samples/day{DAY:02d}.txt"

def part1(input):
    return ""

def part2(input):
    return ""

if __name__ == "__main__":
    util.set_debug(False)
    input = util.read_str_grid(MAIN_PATH)
    sample = util.read_str_grid(SAMPLE_PATH)

    print("PART 1")
    # util.call_and_print(part1, input)
    # util.call_and_print(part1, sample)

    print("PART 2")
    # part2(input)
    # util.call_and_print(part2, input)
    # util.call_and_print(part2, sample)