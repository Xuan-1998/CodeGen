import sys
from functools import lru_cache

@lru_cache(None)
def can_place_mirror(i, j):
    if i >= N or j >= N:  # edge case: reached the end of the grid
        return 1
    if grid[i][j] == '#':  # rock cell, cannot place mirror
        return 0
    empty_to_east = all(grid[k][j] != '#' for k in range(i+1, N))
    return int(empty_to_east)

N = int(sys.stdin.readline())
grid = [list(line.strip()) for line in sys.stdin.readlines()]
T = 1

for _ in range(T):
    count = sum(can_place_mirror(i, j) for i in range(N) for j in range(N))
    print(count)
