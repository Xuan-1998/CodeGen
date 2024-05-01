import sys
from collections import defaultdict

def min_falling_path(grid):
    n = len(grid)
    dp = [[0] * (n - 1) for _ in range(n)]

    # Base case: dp[0][j] = grid[0][j] for all j
    for j in range(n - 1):
        dp[0][j] = grid[0][j]

    for i in range(1, n):
        for k in range(i - 1, -1, -1):
            if k > 0:
                dp[i][k] = min(dp[i-1][k], dp[i][k-1]) + grid[i][k]
            else:
                dp[i][k] = grid[i][k]

    return min(dp[-1])

if __name__ == "__main__":
    n = int(input())
    grid = [list(map(int, input().split())) for _ in range(n)]
    print(min_falling_path(grid))
