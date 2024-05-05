import sys

def min_path_sum(grid):
    m, n = len(grid), len(grid[0])
    dp = [[0] * n for _ in range(m)]

    # Initialize the first row and column
    for i in range(m):
        dp[i][0] = grid[i][0]
    for j in range(n):
        dp[0][j] = grid[0][j]

    # Fill up the rest of the dp table
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = grid[i][j] + min(dp[i-1][j], dp[i][j-1])

    return dp[m-1][n-1]

# Read input from stdin
m, n = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(m)]

# Print the minimum sum to stdout
print(min_path_sum(grid))
