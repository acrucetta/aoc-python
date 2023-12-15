import common.util as util 
import math
import sys
import re

DAY = 12
RELATIVE_PATH = f"../data/day{DAY:02d}.txt"

def part1(filename : str) -> int:
    lines = util.read_strs(filename, sep="\n")
    print(lines)

def part2(input : str) -> int:
    pass

if __name__ == "__main__":
    part1(RELATIVE_PATH)