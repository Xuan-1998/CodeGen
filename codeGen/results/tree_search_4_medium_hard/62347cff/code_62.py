import sys

def min_path_sum(grid):
    m, n = len(grid), len(grid[0])
    dp = [[0] * n for _ in range(m)]

    # Initialize the base case: minimum path sum from top left to cell (i, j)
    dp[0][0] = grid[0][0]

    # Fill up the first column
    for i in range(1, m):
        dp[i][0] = dp[i-1][0] + grid[i][0]

    # Fill up the top row
    for j in range(1, n):
        dp[0][j] = dp[0][j-1] + grid[0][j]

    # Tabulate the solution using a nested loop
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]

    return dp[m-1][n-1]

grid = [list(map(int, input().split())) for _ in range(int(input()))]
print(min_path_sum(grid))
