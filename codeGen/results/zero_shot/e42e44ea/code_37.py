import sys

# Read input from stdin
M, N = map(int, input().split())
grid = []
for _ in range(M):
    row = list(map(int, input().split()))
    grid.append(row)

# Create a DP table to store minimum initial points required
dp = [[0] * N for _ in range(M)]

# Fill up the DP table
for i in range(M):
    for j in range(N):
        if i > 0 and j > 0:
            dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
        elif i == 0 and j > 0:
            dp[i][j] = dp[0][j-1] + grid[i][j]
        elif j == 0 and i > 0:
            dp[i][j] = dp[i-1][0] + grid[i][j]

# Print the minimum initial points required to reach the destination
print(dp[M-1][N-1])
