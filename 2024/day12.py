# Add the parent directory to the Python path so `common` can be found
from collections import deque
import re
import math
import os
import sys
import functools
import itertools
from typing import List, Set, Tuple

from shapely import Point
from util import in_bounds
import util as util

DAY = 12
MAIN_PATH = f"2024/data/day{DAY:02d}.txt"
SAMPLE_PATH = f"2024/samples/day{DAY:02d}.txt"

"""
Step:
- We want to have a visited global set
- Then iterate over each node and find
all nodes that match it. Then once we're
done visiting all of them, we will add them to
a list of visited sets. Then for each of these sets, we will 
calculate the area which is the number of nodes multiplied
by the perimeter, which is each node multiplied by 3

EEEEE
EXXXX
EEEEE
EXXXX
EEEEE

EEXE
EXXE
EEEE
"""


def calculate_perimerter_pt1(coords_set: Set[Tuple[int, int]]) -> int:
    
    perimeter = 0
    for row, col in coords_set:
        for dx, dy in util.CARDINAL_DIRECTIONS:
            adjacent = (row + dx, col + dy)
            if adjacent not in coords_set:
                perimeter += 1
    return perimeter


def calculate_perimeter_pt2(coords_set: Set[Tuple[int, int]]) -> int:
    return


def part1(grid: List[List[int | str]]) -> int:
    visited = set()
    all_paths = []
    max_row, max_col = len(grid), len(grid[0])

    def bfs(start: Tuple[int, int], path: Set[Tuple[int, int]]):
        queue = deque()
        row, col = start
        queue.append((start, grid[row][col]))
        path.add((start))
        while queue:
            (r, c), curr_plant = queue.popleft()
            for dr, dc in util.CARDINAL_DIRECTIONS:  # type: ignore
                new_r, new_c = r + dr, c + dc
                if in_bounds((new_r, new_c), grid):
                    next_plant = grid[new_r][new_c]  # type: ignore
                    if curr_plant == next_plant and (new_r, new_c) not in path:
                        queue.append(((new_r, new_c), next_plant))
                        path.add((new_r, new_c))
                        visited.add((new_r, new_c))
        all_paths.append(path)

    for row in range(max_row):
        for col in range(max_col):
            if (row, col) not in visited:
                bfs((row, col), set())

    res = 0
    for path in all_paths:
        area = len(path)
        res += area * calculate_perimerter_pt1(path)
    return res


def part2(input: str) -> int:
    pass


if __name__ == "__main__":
    util.set_debug(False)
    input = util.read_str_grid(MAIN_PATH)
    sample = util.read_str_grid(SAMPLE_PATH)

    print("PART 1")
    util.call_and_print(part1, input)
    # util.call_and_print(part1, sample)

    print("PART 2")
    # part2(input)
    # util.call_and_print(part2, input)
    # util.call_and_print(part2, sample)
