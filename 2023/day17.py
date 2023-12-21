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


def valid_move(last_three_moves, dr, dc):
    if len(last_three_moves) < 3:
        return True
    else:
        # Check last 3 moves are the same
        are_three_same = all(
            [last_three_moves[i] == last_three_moves[i + 1] for i in range(2)]
        )
        if are_three_same:
            (last_dr, last_dc) = last_three_moves[-1]
            if (last_dr, last_dc) == (dr, dc):
                return False
            # Now we need to verify that the next moves are left or right
            # of the last move e.g., if last move is (0, 1) then next moves can
            # be (1, 0) or (-1, 0)
            if last_dr == 0:
                # Last move was horizontal, next move must be vertical
                return dr != 0
            else:
                # Last move was vertical, next move must be horizontal
                return dc != 0
        return True


def shortest_path(grid: List[List[int]], target: Tuple[int, int]) -> int | float:
    """
    Find the shortest path from the top left to the bottom right of the grid.

    We also need to avoid moving more than 3 consecutive blocks in the same direction.
    If this happens, we need to move in a direction that is perpendicular to the last
    move.
    """
    max_row, max_col = len(grid), len(grid[0])
    min_distance = [[float("inf")] * max_col for _ in range(max_row)]
    min_distance[0][0] = 0
    # (dist, row, col, last_three_moves)
    priority_queue = [(0, 0, 0, [])]

    while priority_queue:
        dist, row, col, last_three_moves = heapq.heappop(priority_queue)

        if (row, col) == target:
            return min_distance[row][col]

        for dr, dc in DIRECTIONS:
            rr, cc = row + dr, col + dc
            if (
                0 <= rr < max_row
                and 0 <= cc < max_col
                and valid_move(last_three_moves, dr, dc)
            ):
                new_dist = dist + grid[rr][cc]
                if new_dist < min_distance[rr][cc]:
                    min_distance[rr][cc] = new_dist
                    new_last_three_moves = last_three_moves[-2:] + [(dr, dc)]
                    heapq.heappush(
                        priority_queue, (new_dist, rr, cc, new_last_three_moves)
                    )
    return min_distance[max_row - 1][max_col - 1]


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
