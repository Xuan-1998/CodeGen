import sys

def min_path_sum(grid):
    m, n = len(grid), len(grid[0])
    dp = [[0] * n for _ in range(m)]

    # Initialize the first row and column
    for i in range(m):
        dp[i][0] = grid[i][0]
    for j in range(n):
        dp[0][j] = grid[0][j]

    # Fill up the rest of the dp array
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]

    return dp[m-1][n-1]

# Read the input from stdin
m, n = map(int, sys.stdin.readline().split())
grid = []
for _ in range(m):
    row = list(map(int, sys.stdin.readline().split()))
    grid.append(row)

# Print the output to stdout
print(min_path_sum(grid))
