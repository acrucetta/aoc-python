from enum import Enum
import sys
import os
from typing import List, Tuple

import numpy as np

parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parent_dir)

import common.util as util

os.chdir(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


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


class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    # Make the point subscriptable
    def __getitem__(self, index: int) -> int:
        if index == 0:
            return self.x
        elif index == 1:
            return self.y
        else:
            raise IndexError("Invalid index")

    def __repr__(self) -> str:
        return f"({self.x}, {self.y})"

    def __eq__(self, other) -> bool:
        return self.x == other.x and self.y == other.y

    def __hash__(self) -> int:
        return hash((self.x, self.y))


class Direction(Enum):
    UP = (0, -1)
    DOWN = (0, 1)
    LEFT = (-1, 0)
    RIGHT = (1, 0)

    def __repr__(self) -> str:
        return f"<{self.value[0]}, {self.value[1]}>"

    # Make the direction subscriptable
    def __getitem__(self, index: int) -> int:
        if index in [0, 1]:
            return self.value[index]
        else:
            raise IndexError("Invalid index")


def handle_empty(direction: Direction) -> List[Direction]:
    return [direction]


def handle_mirror_slash(direction: Direction) -> List[Direction]:
    match direction:
        case Direction.LEFT:
            return [Direction.DOWN]
        case Direction.RIGHT:
            return [Direction.UP]
        case Direction.UP:
            return [Direction.RIGHT]
        case Direction.DOWN:
            return [Direction.LEFT]


def handle_mirror_backslash(direction: Direction) -> List[Direction]:
    match direction:
        case Direction.LEFT:
            return [Direction.UP]
        case Direction.RIGHT:
            return [Direction.DOWN]
        case Direction.UP:
            return [Direction.LEFT]
        case Direction.DOWN:
            return [Direction.RIGHT]


def handle_splitter_horizontal(direction: Direction) -> List[Direction]:
    return (
        [direction]
        if direction in [Direction.LEFT, Direction.RIGHT]
        else [Direction.LEFT, Direction.RIGHT]
    )


def handle_splitter_vertical(direction: Direction) -> List[Direction]:
    return (
        [direction]
        if direction in [Direction.UP, Direction.DOWN]
        else [Direction.UP, Direction.DOWN]
    )


tile_actions = {
    ".": handle_empty,
    "/": handle_mirror_slash,
    "\\": handle_mirror_backslash,
    "-": handle_splitter_horizontal,
    "|": handle_splitter_vertical,
}


def part1(input: List[List[str]]) -> int:
    grid = util.Grid(input)
    energized = dfs(grid)
    return energized


def dfs(
    grid: util.Grid,
    start: Tuple[Tuple[int, int], Direction] = ((0, 0), Direction.RIGHT),
) -> int:
    """
    Traverse the grid using DFS.
    """
    # Start at the top-left (0, 0)
    queue = [start]
    energized = set()
    while queue:
        point, direction = queue.pop(0)
        print(f"Point: {point}, Direction: {direction}")

        # Check if the point is valid
        if not grid.valid(point):
            continue
        try:
            grid.move_coordinates(point, direction)
        except IndexError:
            continue

        energized.add((point, direction))

        # Get the next point in the direction
        next_point = grid.move_coordinates(point, direction)

        tile = grid[next_point]

        # Get the next directions to go
        next_directions = tile_actions[tile](direction)
        for next_direction in next_directions:
            queue.append((next_point, next_direction))

    return len(energized)


def part2(input: List[List[str]]) -> int:
    pass
    return 0


if __name__ == "__main__":
    util.set_debug(False)
    input: List[List[str]] = util.read_str_grid(MAIN_PATH)
    sample: List[List[str]] = util.read_str_grid(SAMPLE_PATH)

    print("PART 1")
    print(part1(sample))
    # part1(input)

    # print("PART 2")
    # part2(input)
    # part2(sample)
