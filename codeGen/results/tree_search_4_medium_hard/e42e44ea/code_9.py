import sys

def min_initial_points(n, m, grid):
    dp = [[0] * m for _ in range(n)]
    dp[0][0] = grid[0][0]

    for i in range(1, n):
        if grid[i][0] > 0:
            dp[i][0] = max(0, dp[i-1][0]) + grid[i][0]
        else:
            break

    for j in range(1, m):
        if grid[0][j] > 0:
            dp[0][j] = max(0, dp[0][j-1]) + grid[0][j]
        else:
            break

    for i in range(1, n):
        for j in range(1, m):
            if grid[i][j] > 0:
                dp[i][j] = min(max(dp[i-1][j], dp[i][j-1]), 0) + grid[i][j]
            else:
                break

    return dp[n-1][m-1]

n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

print(min_initial_points(n, m, grid))
