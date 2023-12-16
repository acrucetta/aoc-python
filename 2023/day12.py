# Add the parent directory to the Python path so `common` can be found
import re
import math
import os
import sys
import functools

parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parent_dir)

import common.util as util

DAY = 12
os.chdir(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
RELATIVE_PATH = f"2023/data/day{DAY:02d}.txt"


@functools.lru_cache(maxsize=None)
def calc(record: list[str], groups: list[int]) -> list[str]:
    if not groups:
        if "#" not in record:
            # Returns true even if the record is empty
            return 1
        else:
            # More damaged sprints that aren't in the groups
            return 0
    if not record:
        # Can't fit, exit
        return 0

    next_char = record[0]
    next_group = groups[0]

    def pound():
        # If the first is a pound, treat the next n
        # chars as pund, where n is the first group
        # number
        this_group = record[:next_group]
        this_group = this_group.replace("?", "#")

        if this_group != next_group * "#":
            return 0

        if len(record) == next_group:
            # Check its the last group
            if len(groups) == 1:
                return 1
            else:
                return 0
        if record[next_group] in "?.":
            return calc(record[next_group + 1 :], groups[1:])

        return 0

    def dot():
        return calc(record[1:], groups)

    if next_char == "#":
        out = pound()

    elif next_char == ".":
        out = dot()

    elif next_char == "?":
        out = pound() + dot()

    else:
        raise ValueError("Invalid character")

    return out


def part1(filename: str) -> int:
    output = 0
    lines = util.read_strs(filename, sep="\n")
    springs = [line.split(" ") for line in lines]
    print(springs[0])

    for spring in springs:
        chars, size = spring[0], spring[1]
        size = [int(s) for s in size.split(",")]
        output += calc(chars, tuple(size))
        print(10 * "-")

    print(">>>", output, "<<<")
    return output


def part2(filename: str) -> int:
    output = 0
    lines = util.read_strs(filename, sep="\n")
    springs = [line.split(" ") for line in lines]
    # Now we need to unfold the springs; on each row we will replace
    # the list of spring conditions with five copies of itself
    for spring in springs:
        chars, size = spring[0], spring[1]
        chars_5x = '?'.join(chars for _ in range(5))
        size_5x = [int(s) for s in size.split(",")] * 5
        print(chars_5x, size_5x)
        temp_output = calc(chars_5x, tuple(size_5x))
        print(temp_output)
        output += temp_output
        print(10 * "-")
    print(">>>", output, "<<<")
    return output


if __name__ == "__main__":
    sample1 = "2023/data/day12_1.txt"
    # output = part1(RELATIVE_PATH)
    output = part2(RELATIVE_PATH)
    # part1(sample1)
    # part2(sample1)
