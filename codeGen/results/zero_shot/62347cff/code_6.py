import sys

def min_path_sum(grid):
    m, n = len(grid), len(grid[0])
    dp = [[0] * (n+1) for _ in range(m+1)]

    # Initialize first row and column
    for i in range(1, m+1):
        dp[i][0] = dp[i-1][0] + grid[i-1][0]
    for j in range(1, n+1):
        dp[0][j] = dp[0][j-1] + grid[0][j-1]

    # Fill up the rest of the DP table
    for i in range(1, m+1):
        for j in range(1, n+1):
            dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i-1][j-1]

    # Return the minimum sum of all numbers along the path
    return dp[m][n]

# Read input and print output
m, n = map(int, sys.stdin.readline().split())
grid = [[int(x) for x in line.split()] for line in sys.stdin.readlines()]
print(min_path_sum(grid))
