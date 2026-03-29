import sys

def min_path_sum(grid):
    m, n = len(grid), len(grid[0])
    dp = [[0] * n for _ in range(m)]

    # Initialize the first row and column
    dp[0][0] = grid[0][0]
    for i in range(1, m):
        dp[i][0] = dp[i-1][0] + grid[i][0]
    for j in range(1, n):
        dp[0][j] = dp[0][j-1] + grid[0][j]

    # Fill the rest of the DP table
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]

    # The minimum sum is stored in the bottom right corner of the DP table
    return dp[m-1][n-1]

# Read input from stdin
m, n = map(int, sys.stdin.readline().split())
grid = [[int(x) for x in sys.stdin.readline().split()] for _ in range(m)]

# Print the output to stdout
print(min_path_sum(grid))
