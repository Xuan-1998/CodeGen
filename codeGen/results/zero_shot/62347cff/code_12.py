import sys

# Read input from stdin
m, n = map(int, sys.stdin.readline().split())
grid = []
for _ in range(m):
    row = list(map(int, sys.stdin.readline().split()))
    grid.append(row)

# Initialize dp table with all zeros (min sum for each cell)
dp = [[0] * n for _ in range(m)]

# Calculate min sum for each cell
for i in range(m):
    for j in range(n):
        if i == 0 and j == 0:  # Top-left corner
            dp[i][j] = grid[i][j]
        elif i == 0:  # Top edge
            dp[i][j] = dp[i][j-1] + grid[i][j]
        elif j == 0:  # Left edge
            dp[i][j] = dp[i-1][j] + grid[i][j]
        else:
            dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]

# Print the minimum sum for the bottom-right corner (the final cell)
print(dp[m-1][n-1])
