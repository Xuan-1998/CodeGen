import sys

def min_falling_path_sum(grid):
    n = len(grid)
    dp = [[0] * (n + 1) for _ in range(n)]

    for i in range(n - 2, -1, -1):
        for k in range(i + 1):
            if k == 0:
                dp[i][k] = grid[i][k]
            else:
                dp[i][k] = min(dp[i+1][j] + grid[i][j] for j in range(n)) + grid[i][k]

    return min(dp[0])

grid = [list(map(int, input().split())) for _ in range(int(input()))]
print(min_falling_path_sum(grid))
