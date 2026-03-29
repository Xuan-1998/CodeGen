import sys
from collections import memoize

@memoize
def dp(i, j):
    if i == 0 or j == 0:
        return 0
    return min(dp(i-1, j) + grid[i][j], dp(i, j-1) + grid[i][j])

N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]

print(dp(N-1, M-1))
