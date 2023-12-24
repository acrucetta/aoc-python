from typing import List, Tuple
import util as util
from dataclasses import dataclass
import colorsys as cs
import numpy as np

DAY = 18
MAIN_PATH = f"2023/data/day{DAY:02d}.txt"
SAMPLE_PATH = f"2023/data/day{DAY:02d}-sample.txt"

"""
Day 18: Lavaduct Lagoon

We have excavation plans for a lava factory. We receive a series of instructions:

R 6 (#70c710)
D 5 (#0dc571)
L 2 (#5713f0)
D 2 (#d2c081)
R 2 (#59c680)
D 2 (#411b91)
L 5 (#8ceee2)
U 2 (#caa173)
L 1 (#1b58a2)
U 2 (#caa171)
R 2 (#7807d2)
U 3 (#a77fa3)
L 2 (#015232)
U 2 (#7a21e3)

We assume we start at the 0,0 coordinates and then proceed to follow the instructions.
R means east, L means west, U means north, and D means south. Once we dig the trenches
we will fill up the inside of the trenches with lava and count the number of # in the 
grid.

Approach:
- Parse each instruction into a tuple (direction, distance)
- Fill up the grid with the instructions
- Find the encircled area in the grid
- Fill it up and count the number of # in the grid
"""


@dataclass
class Instruction:
    direction: str
    distance: int
    hex: str

    def coord_from_direction(self):
        match self.direction:
            case "R":
                return (1, 0)
            case "L":
                return (-1, 0)
            case "U":
                return (0, -1)
            case "D":
                return (0, 1)


def parse_instructions(input: List[str]) -> List[Instruction]:
    instructions = []
    for line in input:
        direction, distance, rgb = line.split()
        instructions.append(Instruction(direction, int(distance), rgb))
    return instructions


def parse_hex_instructions(input: List[str]) -> List[Tuple[int, Tuple[int, int]]]:
    instructions = []
    # The last hexadecimal digit encodes the direction to dig:
    # 0 means R, 1 means D, 2 means L, and 3 means U.
    dist_map = {"0": (1, 0), "1": (0, 1), "2": (-1, 0), "3": (0, -1)}
    for line in input:
        _, _, hex = line.split()
        # Remove (, ) and # from hex
        # (#70c710)
        hex = hex[2:-1]
        hex_distance = int(hex[:5], 16)
        direction = dist_map[hex[-1]]
        instructions.append((hex_distance, direction))
    return instructions


def calculate_area(corners: List[Tuple[int, int]]) -> int:
    # We need to find the area of the polygon
    # https://www.mathopenref.com/coordpolygonarea.html
    # We need to find the sum of the products of the coordinates
    # and the sum of the products of the coordinates shifted by 1
    # in a circular fashion
    n = len(corners)
    area = 0
    for i in range(n):
        x1, y1 = corners[i]
        x2, y2 = corners[(i + 1) % n]
        area += (x1 * y2) - (x2 * y1)
    return abs(area) // 2


def part1(input: List[str]) -> int:
    instructions = parse_instructions(input)
    grid = [["." for _ in range(1000)] for _ in range(1000)]
    curr_coord = (500, 500)
    corners = []
    for instruction in instructions:
        print("Instruction:", instruction)
        x, y = curr_coord
        dx, dy = instruction.coord_from_direction()
        # We want to mark the coordinates from curr_coord to
        # the next coordinate
        for _ in range(instruction.distance):
            x, y = x + dx, y + dy
            grid[y][x] = "#"
        corners.append((x, y))
        curr_coord = (x, y)
    # Apply pick's theorem to find the number of # in the grid
    boundary_points = sum(row.count("#") for row in grid)
    area = calculate_area(corners)
    interior_points = (area + 1) - (boundary_points // 2)
    return boundary_points + interior_points


def part2(input: List[str]) -> int:
    instructions = parse_hex_instructions(input)
    curr_coord = (0, 0)
    boundaries = []
    corners = []
    for distance, direction in instructions:
        x, y = curr_coord
        dx, dy = direction
        # We want to mark the coordinates from curr_coord to
        # the next coordinate
        for _ in range(distance):
            x, y = x + dx, y + dy
            boundaries.append((x, y))
        corners.append((x, y))
        curr_coord = (x, y)
    # Apply pick's theorem to find the number of # in the grid
    boundary_points = len(boundaries)
    area = calculate_area(corners)
    interior_points = (area + 1) - (boundary_points // 2)
    return boundary_points + interior_points


if __name__ == "__main__":
    util.set_debug(False)
    input = util.read_strs(MAIN_PATH, sep="\n")
    sample = util.read_strs(SAMPLE_PATH, sep="\n")

    print("PART 1")
    # util.call_and_print(part1, input)
    # util.call_and_print(part1, sample)

    print("PART 2")
    util.call_and_print(part2, input)
    util.call_and_print(part2, sample)
