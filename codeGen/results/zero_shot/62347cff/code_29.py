import sys

def min_path_sum(grid):
    m, n = len(grid), len(grid[0])
    dp = [[0] * n for _ in range(m)]

    # Initialize the first row and column
    dp[0][j] = grid[0][j] for j in range(n)
    dp[i][0] = grid[i][0] for i in range(m)

    # Fill up the DP table
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]

    return dp[m-1][n-1]

grid = []
for _ in range(int(input())):
    row = list(map(int, input().split()))
    grid.append(row)

print(min_path_sum(grid))
