import sys
from collections import defaultdict

def min_points_required(grid):
    N, M = len(grid), len(grid[0])
    memo = defaultdict(int)

    def dp(i, j):
        if i == 0 and j == 0:
            return grid[i][j]
        if (i, j) in memo:
            return memo[(i, j)]
        if i > 0 and j > 0:
            memo[(i, j)] = min(dp(i-1, j), dp(i, j-1)) + grid[i][j]
        elif i > 0:
            memo[(i, j)] = dp(i-1, j) + grid[i][j]
        else:
            memo[(i, j)] = dp(i, j-1) + grid[i][j]
        return memo[(i, j)]

    return dp(N-1, M-1)

N, M = map(int, input().split())
grid = [[int(x) for x in input().split()] for _ in range(N)]
print(min_points_required(grid))
