import sys

def min_path_sum(grid):
    m, n = len(grid), len(grid[0])
    dp = [[0] * n for _ in range(m)]

    # Initialize the first row and column
    for i in range(m):
        dp[i][0] = grid[i][0]
    for j in range(n):
        dp[0][j] = grid[0][j]

    # Fill in the rest of the dp table
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = grid[i][j] + min(dp[i-1][j], dp[i][j-1])

    # The minimum sum is stored in the bottom right cell of the dp table
    return dp[m-1][n-1]

# Read input from stdin and print output to stdout
m, n = map(int, sys.stdin.readline().split())
grid = [list(map(int, line.split())) for line in sys.stdin.read().strip().split('\n')]
print(min_path_sum(grid))
