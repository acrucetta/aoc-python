# Add the parent directory to the Python path so `common` can be found
import re
import math
import os
import sys
import functools
import itertools
from typing import List, Tuple
import util as util
from dataclasses import dataclass

DAY = 14
MAIN_PATH = f"2024/data/day{DAY:02d}.txt"
SAMPLE_PATH = f"2024/samples/day{DAY:02d}.txt"

"""
Challenge:
s
p=2,4 v=2,-3
p=9,5 v=-3,-3

Each robot's position is given as p=x,y where x represents the 
number of tiles the robot is from the left wall and y represents 
the number of tiles from the top wall

Each robot's velocity is given as v=x,y where x and y are given 
in tiles per second.

Positive x means the robot is moving to the right, 
and positive y means the robot is moving down.

To determine the safest area, count the number of robots in 
each quadrant after 100 seconds. Robots that are exactly in 
the middle (horizontally or vertically) don't count as being 
in any quadrant, so the only relevant robots are.

Multiplying these together gives a total safety factor of 12.

Goal: Where will the robots be after 100 seconds?

Steps:
- Parse the input into positions (x,y) and moves (vx,vy)
- Simulate each position and handle max width and height.
"""

MAX_WIDTH = 101
MAX_HEIGHT = 103

Position = Tuple[int, int]
Velocity = Tuple[int, int]


class Robot:
    def __init__(self, position: Position, velocity: Velocity) -> None:
        self.position: Position = position
        self.velocity: Velocity = velocity

    def move(self, seconds: int = 1):
        for _ in range(seconds):
            dx = (self.position[0] + self.velocity[0]) % MAX_WIDTH
            dy = (self.position[1] + self.velocity[1]) % MAX_HEIGHT
            self.position = (dx, dy)


class Grid:
    def __init__(self, robots: List[Robot]) -> None:
        self.max_width = MAX_WIDTH
        self.max_height = MAX_HEIGHT
        self.robots = robots

    def move_all(self, seconds: int):
        for robot in self.robots:
            robot.move(seconds)

    def get_score(self) -> int:
        """
        The score is calculated by the number of robots
        in each quadrant multiplied by each other.
        """
        blocked_x, blocked_y = MAX_WIDTH // 2, MAX_HEIGHT // 2
        q1s = list(
            filter(
                lambda robot: robot.position[0] < blocked_x
                and robot.position[1] < blocked_y,
                self.robots,
            )
        )
        q2s = list(
            filter(
                lambda robot: robot.position[0] > blocked_x
                and robot.position[1] < blocked_y,
                self.robots,
            )
        )
        q3s = list(
            filter(
                lambda robot: robot.position[0] < blocked_x
                and robot.position[1] > blocked_y,
                self.robots,
            )
        )
        q4s = list(
            filter(
                lambda robot: robot.position[0] > blocked_x
                and robot.position[1] > blocked_y,
                self.robots,
            )
        )
        score = len(q1s) * len(q2s) * len(q3s) * len(q4s)
        return score

    def __str__(self):
        grid = [["." for _ in range(self.max_width)] for _ in range(self.max_height)]
        position_count = {}
        for robot in self.robots:
            x, y = robot.position
            if (x, y) in position_count:
                position_count[(x, y)] += 1
            else:
                position_count[(x, y)] = 1
        for (x, y), count in position_count.items():
            grid[y][x] = str(count) if count < 10 else "9"
        grid_str = "\n".join("".join(row) for row in grid)
        return f"{grid_str}"


def parse_robot(line: str):
    """
    Input:
        p=2,4 v=2,-3
    Output:
        (2,4),(2,-3)
    """
    reg = "p=(-?\d+),(-?\d+) v=(-?\d+),(-?\d+)"
    matches = re.findall(reg, line)
    match = matches[0]
    robot = Robot((int(match[0]), int(match[1])), (int(match[2]), int(match[3])))
    return robot


def part1(input: str) -> int:
    robots = []
    for line in input:
        robots.append(parse_robot(line))
    grid = Grid(robots)
    for sec in range(25):
        print(f"Second: {sec}")
        grid.move_all(1)
        print(grid)
    score = grid.get_score()
    return score


def part2(input: str) -> int:
    pass


if __name__ == "__main__":
    util.set_debug(False)
    input = util.read_strs(MAIN_PATH, "\n")
    sample = util.read_strs(SAMPLE_PATH, "\n")

    print("PART 1")
    util.call_and_print(part1, input)
    # util.call_and_print(part1, sample)

    print("PART 2")
    # part2(input)
    util.call_and_print(part2, input)
    # util.call_and_print(part2, sample)
