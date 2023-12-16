# Add the parent directory to the Python path so `common` can be found
import re
import math
import common.util as util
import os
import sys
import functools

parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parent_dir)


DAY = 12
os.chdir(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
RELATIVE_PATH = f"2023/data/day{DAY:02d}.txt"

chars = [".", "#", "?"]

output = 0


def is_valid(spring: list[str], size: list[int]) -> bool:
    counts = []
    cnt = 0
    for char in spring:
        if char == "#":
            cnt += 1
            continue
        counts.append(cnt)
        cnt = 0
    return counts == size


@functools.lru_cache(maxsize=None)
def calc(record: list[str], groups: list[int]) -> list[str]:
    next_char = record[0]
    next_group = groups[0]

    def pound():
        return 0
    
    def dot():
        return 0
    
    if next_char == "#":
        out = pound()

    elif next_char == ".":
        out = dot()
    
    elif next_char == "?":
        out = pound() + dot()

    else:
        raise ValueError("Invalid character")
    
    print(record, groups, "->", out)
    return out

    


def part1(filename: str) -> int:
    lines = util.read_strs(filename, sep="\n")
    springs = [line.split(" ") for line in lines]
    print(springs[0])
    for spring in springs:
        chars, size = spring[0], spring[1]
        size = [int(s) for s in size.split(",")]
        output += calc(chars, tuple(size))
        print(10*"-")



def part2(input: str) -> int:
    pass


if __name__ == "__main__":
    part1(RELATIVE_PATH)
