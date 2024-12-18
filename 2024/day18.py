# Add the parent directory to the Python path so `common` can be found
from collections import deque
import re
import math
import os
import sys
import functools
import itertools
from typing import Tuple
import util as util

DAY = 18
MAIN_PATH = f"2024/data/day{DAY:02d}.txt"
SAMPLE_PATH = f"2024/samples/day{DAY:02d}.txt"

"""
Challenge:
- Each byte position is given as an X,Y coordinate (col,row)
- Need to go from 0,0 to 70,70 (or 6,6)
- Bytes will fall into the map and make obstacles
- Find the shortest path from the top left corner
to the exit.

"""


def part1(input: str, bytes: int, max_size: int) -> int:
    corrupted = set([tuple(map(int, pair.split(","))) for pair in input][:bytes])
    target = (max_size, max_size)
    queue = deque()
    queue.append([0, 0, 0])
    seen = {(0, 0)}
    while queue:
        (row, col, dist) = queue.popleft()

        if (col, row) == target:
            return dist

        for dr, dc in util.CARDINAL_DIRECTIONS:
            rr, cc = (row + dr), (col + dc)
            if (
                0 <= rr <= max_size
                and 0 <= cc <= max_size
                and (rr, cc) not in seen
                and (cc, rr) not in corrupted
            ):
                queue.append((rr, cc, dist + 1))
                seen.add((rr, cc))
    return -1


def part2(input: str, max_size: int) -> Tuple[int, int]:
    corrupted = [tuple(map(int, pair.split(","))) for pair in input]
    for bytes, _ in enumerate(corrupted):
        print(f"Trying with #{bytes} bytes")
        dist = part1(input, bytes, max_size)
        if dist == -1:
            return corrupted[bytes - 1]  # type: ignore
    return (-1, -1)


if __name__ == "__main__":
    util.set_debug(False)
    input = util.read_strs(MAIN_PATH)
    sample = util.read_strs(SAMPLE_PATH)

    print("PART 1")
    util.call_and_print(part1, sample, 12, 6)
    util.call_and_print(part1, input, 1024, 70)

    print("PART 2")
    # part2(input)
    util.call_and_print(part2, input, 70)
    # util.call_and_print(part2, sample, 6)
