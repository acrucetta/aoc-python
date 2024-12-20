# Add the parent directory to the Python path so `common` can be found
from collections import deque
import re
import math
import os
import sys
import functools
import itertools
from typing import List, Tuple
import util as util
import copy

DAY = 20
MAIN_PATH = f"2024/data/day{DAY:02d}.txt"
SAMPLE_PATH = f"2024/samples/day{DAY:02d}.txt"

"""
Problem:
We have a map of a racetrack. It has a start (S) and end (E),
as well as walls (#) and paths (.)

Each move takes 1 picosecond. The fastest time in the sample is
84 ps. 

Once within the race, we will disable walls for 2 moves. This means
we can go through any walls. We want to find out how many cheats
would saveu s at least 100 picoseconds.

Steps:
- Get the baseline time to complete the course. (We can do BFS or a simple iteration)
- For obstacles around the path, for two turns, remove any blocks in the walls.
    - We can do this by getting the list of visited nodes, and removing obstacles along
    the path in +/-2 in each direction, then seeing how long it will take.
    - We can have a base traversal, and then one to update the grid given the visited
    coordinates.
"""


def traverse_grid(grid: List[List[str]], start: Tuple[int, int]) -> Tuple[int, set]:
    max_row, max_col = len(grid), len(grid[0])
    queue = deque()
    # row, col, picoseconds
    start_r, start_c = start
    queue.append([start_r, start_c, 0])
    seen = {(start_r, start_c)}
    while queue:
        (row, col, dist) = queue.popleft()

        if grid[row][col] == "E":
            return dist, seen

        for dr, dc in util.CARDINAL_DIRECTIONS:
            rr, cc = (row + dr), (col + dc)
            if (
                0 <= rr <= max_row
                and 0 <= cc <= max_col
                and (rr, cc) not in seen
                and grid[rr][cc] != "#"
            ):
                queue.append((rr, cc, dist + 1))
                seen.add((rr, cc))
    return (0, set())


def build_obstacle_list(grid, path):
    return 0


def part1(input: List[List[str]]) -> int:
    start = (-1, -1)
    wall_coordinates = []
    for row, row_vals in enumerate(input):
        for col, val in enumerate(row_vals):
            if val == "S":
                start = (row, col)
            elif val == "#":
                wall_coordinates.append((row, col))
    baseline_ps, path = traverse_grid(input, start)

    # With the baseline path, we want to update the grid by removing
    # 2 obstacles (#) from it and traversing it again. We can build
    # a list of potential obstacle pairs we want to remove and iterate
    # over it as we update the grid
    
    # Run a N choose 2 of the wall coordinates
    print(f"Total wall coordinates:{len(wall_coordinates)}")
    obstacle_list = list(itertools.combinations(wall_coordinates,2))
    print(f"Obstacle length:{len(obstacle_list)}")
    speeds = []
    for i, (obs1, obs2) in enumerate(obstacle_list):
        print(f"Progress:{i}")
        new_grid = copy.deepcopy(input)
        new_grid[obs1[0]][obs1[1]] == "."
        new_grid[obs2[0]][obs2[1]] == "."
        new_ps, _ = traverse_grid(new_grid, start)
        speeds.append(new_ps)
    return len(list(filter(lambda x: x > 100, speeds)))


def part2(input: List[List[str]]) -> int:
    return 0


if __name__ == "__main__":
    util.set_debug(False)
    input = util.read_str_grid(MAIN_PATH)
    sample = util.read_str_grid(SAMPLE_PATH)

    print("PART 1")
    # util.call_and_print(part1, sample)
    util.call_and_print(part1, input)

    print("PART 2")
    # util.call_and_print(part2, input)
    # util.call_and_print(part2, sample)
