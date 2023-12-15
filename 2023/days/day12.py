import common.util as util
import math
import sys
import re

DAY = 12

def part1(filenam) -> int:
    lines = util.read_strs(f"{DAY}.txt", sep="\n")
    print(lines)

def part2(input : str) -> int:
    pass

if __name__ == "__main__":
    util.set_debug(False)
    util.set_day(DAY)
    input = util.get_input()
    util.call_and_print(part1, input)
    util.call_and_print(part2, input)