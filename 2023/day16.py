from collections import deque
from enum import Enum
import sys
import os
from typing import List, Tuple
import util
import numpy as np


"""
Day 16: The Floor Will be Lava

We receive a grid containing empty space (.) mirrors (/ and \)
and splitters (| and -). 

Each tile converts some of the beam's light into heat to melt the
rock in the cavern.

Beam behavior:
- Empty space = continue same direction
- Mirror (/ or \) = change direction 90 degrees depending on the angle
    - / -> upward if coming from left, downward if coming from right
    - \ -> upward if coming from right, downward if coming from left
- Splitter (| or -)
    - - -> continue straight if coming from left or right
    - | -> continue straight if coming from up or down
    - - -> split into two beams if coming from up or down
    - | -> split into two beams if coming from left or right

Beam caveats:
- Beams do not interact with each other
- A tile is energized if that tile has at least one beam on it

.|...\....
|.-.\.....
.....|-...
........|.
..........
.........\
..../.\\..
.-.-/..|..
.|....-|.\
..//.|....

We want a count of the number of energized tiles. We assume
the beam starts in the top-left heading right.

Approach:
- We need to keep track of the energized tiles; we can use a set
- We want to traverse a graph given specific rules for each tile
    Based on each rule we will pick a direction to go
    To pick the direction we need to know the tile type; 
    and the direction the beam is coming from. With these two
    we can determine the direction to go next.
- We will need to manage multiple beams at once; that is, 
    we can have many iterations of the beam.
    
Data Structures:
- We can use a 2D array to represent the grid
- We can use a set to represent the energized tiles

Traversal:
- We can use a queue to manage the beams and the directions we need to go
  i.e., we can have two valid directions when we add a value to the queue
- We will implement a BFS traversal
"""

DAY = 16
MAIN_PATH = f"2023/data/day{DAY:02d}.txt"
SAMPLE_PATH = f"2023/data/day{DAY:02d}-sample.txt"


def part1(input: List[List[str]]) -> int:
    arr = np.array(input)
    energized = dfs(arr)
    return energized


def dfs(
    grid: np.ndarray,
    start: Tuple[Tuple[int, int], Tuple[int, int]] = ((0, -1), (0, 1)),
) -> int:
    """
    Traverse the grid using DFS.
    """
    max_x, max_y = np.shape(grid)
    queue = deque([start])
    visited = set()
    while queue:
        (row, col), (di, dj) = queue.pop()
        next_row = row + di
        next_col = col + dj
        if ((next_row, next_col), (di,dj)) in visited:
            continue
        if not (0 <= next_row < max_x and 0 <= next_col < max_y):
            continue
        visited.add(((next_row, next_col), (di, dj)))
        tile = grid[next_row, next_col]
        match tile:
            case "/":
                di, dj = -dj, -di
            case "\\":
                di, dj = dj, di
            case "-":
                if di:
                    di, dj = 0, 1
                    queue.append(((next_row, next_col), (0, -1)))
            case "|":
                if dj:
                    di, dj = 1, 0
                    queue.append(((next_row, next_col), (-1, 0)))
            case ".":
                di, dj = di, dj
            case _:
                raise ValueError(f"Invalid tile: {tile}")
        queue.append(((next_row, next_col), (di, dj)))

    return len(set([p for p, _ in visited]))


def part2(input: List[List[str]]) -> int:
    arr = np.array(input)
    max_x, max_y = np.shape(arr)
    energized = 0
    for x in range(max_x):
        energized = max(energized, dfs(arr, start=((x, -1), (0, 1))))
        energized = max(energized, dfs(arr, start=((x, max_y), (0, -1))))
    for y in range(max_y):
        energized = max(energized, dfs(arr, start=((-1, y), (1, 0))))
        energized = max(energized, dfs(arr, start=((max_x, y), (-1, 0))))
    print(energized)
    return energized


if __name__ == "__main__":
    util.set_debug(False)
    input: List[List[str]] = util.read_str_grid(MAIN_PATH)
    sample: List[List[str]] = util.read_str_grid(SAMPLE_PATH)

    print("PART 1")
    print(part1(sample))
    print(part1(input))

    print("PART 2")
    part2(input)
    part2(sample)
