import sys
from functools import lru_cache

N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(M)]

@lru_cache(None)
def dfs(i, j, points):
    if i == M-1 and j == N-1:
        return 0
    if i > M-1 or j > N-1:
        return -sys.maxsize

    min_points = -sys.maxsize
    if i > 0:
        min_points = max(min_points, dfs(i-1, j, points-grid[i][j]))
    if j > 0:
        min_points = max(min_points, dfs(i, j-1, points-grid[i][j]))

    return min_points + grid[i][j]

print(dfs(0, 0, 0))
