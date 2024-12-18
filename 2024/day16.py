# Add the parent directory to the Python path so `common` can be found
import heapq
import re
import math
import os
import sys
import functools
import itertools
from typing import List, Tuple
import util as util

DAY = 16
MAIN_PATH = f"2024/data/day{DAY:02d}.txt"
SAMPLE_PATH = f"2024/samples/day{DAY:02d}.txt"

"""
Steps:
- Find the most efficient path from S to E
- Cost:
    - If we move forward, it costs 1 point
    - If we rotate (i.e., turn 90 degrees), it costs 1000 points

Approach:
- Use Dijkstra to calculate the most cost efficient path
at each step
"""


def shortest_path(
    grid: List[List[str]], start: Tuple[int, int], end: Tuple[int, int]
) -> int | float:
    """
    Find the shortest path from the top left to the bottom right of the grid.

    Notes:
    - Update to account for directions, if we change directions, add 1000, else 1
    """
    max_row, max_col = len(grid), len(grid[0])
    start_r, start_c = start

    # (score, row, col, prev_dr, prev_dc)
    min_score = {}
    priority_queue = [(0, start_r, start_c, 0, 1)]
    while priority_queue:
        score, row, col, prev_dr, prev_dc = heapq.heappop(priority_queue)

        if (row, col) == end:
            return score

        state = ((row, col), (prev_dr, prev_dc))
        if state in min_score and score >= min_score[state]:
            continue

        min_score[state] = score

        for dr, dc in util.CARDINAL_DIRECTIONS:
            rr, cc = row + dr, col + dc
            if 0 <= rr < max_row and 0 <= cc < max_col and grid[rr][cc] != "#":
                new_score = score + (1 if (dr, dc) == (prev_dr, prev_dc) else 1001)
                heapq.heappush(priority_queue, (new_score, rr, cc, dr, dc))
    return float("inf")


def part1(grid: List[List[str]]) -> int:
    start = (0, 0)
    end = (0, 0)
    for row, row_vals in enumerate(grid):
        for col, val in enumerate(row_vals):
            if val == "S":
                start = (row, col)
            elif val == "E":
                end = (row, col)
    min_score = int(shortest_path(grid, start, end))
    return min_score


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
    util.call_and_print(part2, input)
    # util.call_and_print(part2, sample)
