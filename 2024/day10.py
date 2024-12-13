from collections import deque
from typing import List, Tuple
from dataclasses import dataclass
import util as util
import colorsys as cs
import numpy as np

DAY = 10
MAIN_PATH = f"2024/data/day{DAY:02d}.txt"
SAMPLE_PATH = f"2024/samples/day{DAY:02d}.txt"

"""
For each trailhead we need to calculate the score, i.e., how
many nodes with a 9 can we reach from that trailhead.
"""

Point = Tuple[int, int]
Grid = List[List[int]]


def in_bounds(point: Point, grid: Grid):
    row, col = point
    max_row, max_col = len(grid) - 1, len(grid[0]) - 1
    if 0 <= row <= max_row and 0 <= col <= max_col:
        return True
    return False


def get_zeros(grid: Grid) -> List[Point]:
    starts = []
    for r, row in enumerate(grid):
        for c, h in enumerate(row):
            if h == 0:
                starts.append((r, c))
    return starts


def get_score_pt1(start: Point, grid: Grid) -> int:
    queue = deque()
    queue.append((start, 0))
    visited = set()
    nines = set()
    while queue:
        (row, col), curr_height = queue.popleft()
        if curr_height == 9:
            nines.add((row, col))
            continue
        for dr, dc in util.CARDINAL_DIRECTIONS:  # type: ignore
            new_r, new_c = row + dr, col + dc
            if in_bounds((new_r, new_c), grid):
                new_height = grid[new_r][new_c]
                if (new_height - curr_height) == 1 and (new_r, new_c) not in visited:
                    queue.append(((new_r, new_c), new_height))
                    visited.add((new_r, new_c))
    return len(nines)


def get_score_pt2(start: Point, grid: Grid) -> int:
    unique_paths = set()
    visited = set()

    def dfs(r, c, curr_path):
        nonlocal unique_paths
        if grid[r][c] == 9:
            unique_paths.add(curr_path)
            return
        for dr, dc in util.CARDINAL_DIRECTIONS:  # type: ignore
            new_r, new_c = r + dr, c + dc
            if in_bounds((new_r, new_c), grid) and (new_r, new_c) not in visited:
                curr_height = grid[r][c]
                new_height = grid[new_r][new_c]
                if (new_height - curr_height) == 1:
                    visited.add((new_r, new_c))
                    dfs(new_r, new_c, curr_path + ((new_r,new_c),))
                    visited.remove((new_r, new_c))

    visited.add(start)
    dfs(start[0], start[1], (start,))
    return len(unique_paths)


def part1(grid):
    # Convert to int grid
    grid = [[int(cell) for cell in row] for row in grid]

    # Find the start nodes, i.e., the edges with 0
    starts = get_zeros(grid)
    # For each of the starts, calculate the scores
    score = 0
    for r, c in starts:
        score += get_score_pt1((r, c), grid)
    return score


def part2(grid):
    # Convert to int grid
    grid = [[int(cell) for cell in row] for row in grid]

    # Find the start nodes, i.e., the edges with 0
    starts = get_zeros(grid)
    # For each of the starts, calculate the scores
    score = 0
    for r, c in starts:
        score += get_score_pt2((r, c), grid)
    return score


if __name__ == "__main__":
    util.set_debug(False)
    input = util.read_str_grid(MAIN_PATH)
    sample = util.read_str_grid(SAMPLE_PATH)

    print("PART 1")
    # util.call_and_print(part1, input)
    # util.call_and_print(part1, sample)

    print("PART 2")
    # part2(input)
    util.call_and_print(part2, input)
    # util.call_and_print(part2, sample)
