import sys

def min_path_sum(grid):
    m, n = len(grid), len(grid[0])
    dp = [[0] * n for _ in range(m)]

    # Base case: top left corner
    dp[0][0] = grid[0][0]

    # Fill up the first row
    for j in range(1, n):
        dp[0][j] = dp[0][j-1] + grid[0][j]

    # Fill up the first column
    for i in range(1, m):
        dp[i][0] = dp[i-1][0] + grid[i][0]

    # Fill up the rest of the grid
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]

    return dp[m-1][n-1]

# Read input from stdin
m, n = map(int, sys.stdin.readline().split())
grid = [[int(x) for x in line.split()] for line in [sys.stdin.readline() for _ in range(m)]]

# Print the answer to stdout
print(min_path_sum(grid))
