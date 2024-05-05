import sys

def min_path_sum(grid):
    m, n = len(grid), len(grid[0])
    dp = [[0] * n for _ in range(m)]

    # Initialize base cases
    dp[0][j] = grid[0][j] for j in range(n)
    dp[i][0] = grid[i][0] for i in range(m)

    # Fill in dp array from top to bottom and left to right
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]

    return dp[m-1][n-1]

# Read input from stdin
grid = [[int(x) for x in line.split()] for line in sys.stdin.readlines()]

print(min_path_sum(grid))
