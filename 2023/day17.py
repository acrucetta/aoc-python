import util as util
from typing import List, Tuple
import heapq

"""
Day 17: Clumsy Crucible

Find the best way to get the crucible from the lava pool
to the machine parts factory. We need to minimize the heat loss
while choosing a route that doesn't require the crucible to go
in a straight line for too long.

E.g.,

2413432311323
3215453535623
3255245654254
3446585845452
4546657867536
1438598798454
4457876987766
3637877979653
4654967986887
4564679986453
1224686865563
2546548887735
4322674655533

Each city block is marked by a single digit that represents the amount
of heat loss if the crucible enters that block. The starting point, the
lava is the top-left city block. (doesn't count unless you vit it again)

Find the path from top left to bottom right that minimizes heat loss.

Approach:

- Use Dijkstra's algorithm to find the path from 0,0 to max_row, max_col that minimizes
  heat loss (aka digits)

Caveat:
- We can never move more than 3 consecutive blocks in the same direction.
"""

DAY = 17
MAIN_PATH = f"2023/data/day{DAY:02d}.txt"
SAMPLE_PATH = f"2023/data/day{DAY:02d}-sample.txt"

DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def valid_move(move_history, new_move):
    if len(move_history) >= 3:
        if move_history[-3:] == [new_move] * 3:
            # We can't move in the same direction 3 times in a row
            return False
        if move_history[-1] == (-new_move[0], -new_move[1]):
            # We can't move in the opposite direction of the last move
            return False
    return True


def print_path(grid, path):
    dir_symbols = {(1, 0): "v", (0, 1): ">", (-1, 0): "^", (0, -1): "<"}
    for r, c, dr, dc in path:
        if (dr, dc) in dir_symbols:
            grid[r][c] = dir_symbols[(dr, dc)]
    print_grid(grid)


def print_grid(grid) -> None:
    rows = ["\t".join(str(x) for x in row) for row in grid]
    print("\n".join(rows))


def shortest_path(grid: List[List[int]], target: Tuple[int, int]) -> int | float:
    """
    Find the shortest path from the top left to the bottom right of the grid.

    We also need to avoid moving more than 3 consecutive blocks in the same direction.
    If this happens, we need to move in a direction that is perpendicular to the last
    move.
    """
    max_row, max_col = len(grid), len(grid[0])
    min_heat = [[float("inf")] * max_col for _ in range(max_row)]
    min_heat[0][0] = 0
    # (heat, row, col, moves)
    priority_queue = [(0, 0, 0, 0, 0, [])]
    seen = set()

    while priority_queue:
        heat, row, col, dr, dc, moves = heapq.heappop(priority_queue)

        if (row, col) == target:
            return min_heat[row][col]
        if ((row, col), (dr, dc)) in seen:
            continue
        seen.add(((row, col), (dr, dc)))

        for dr, dc in DIRECTIONS:
            rr, cc = row + dr, col + dc
            if 0 <= rr < max_row and 0 <= cc < max_col and valid_move(moves, (dr, dc)):
                new_heat = heat + grid[rr][cc]
                if new_heat < min_heat[rr][cc]:
                    min_heat[rr][cc] = new_heat
                    new_moves = moves + [(dr, dc)]
                    heapq.heappush(
                        priority_queue, (new_heat, rr, cc, dr, dc, new_moves)
                    )
    return min_heat[max_row - 1][max_col - 1]


def part1(input: List[List[int]]) -> int | float:
    target = (len(input) - 1, len(input[0]) - 1)
    min_distance = shortest_path(input, target)
    print(min_distance)
    return min_distance


def part2(input: str) -> int:
    return 0


if __name__ == "__main__":
    util.set_debug(False)
    # input = util.read_strs(MAIN_PATH)
    sample = util.read_str_grid(SAMPLE_PATH)
    sample_int = [[int(c) for c in row] for row in sample]

    print("PART 1")
    # part1(input)
    part1(sample_int)

    # print("PART 2")
    # part2(input)
    # part2(sample)
