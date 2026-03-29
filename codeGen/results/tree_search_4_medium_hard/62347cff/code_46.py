# Initialize the dp table with the same size as the grid
dp = [[0]*n for _ in range(m)]

# Fill the first row and column of the dp table
for i in range(m):
    dp[i][0] = grid[i][0]
for j in range(n):
    dp[0][j] = grid[0][j]

# Use memoization to fill the rest of the dp table
for i in range(1, m):
    for j in range(1, n):
        dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]

# The minimum path sum from the top left corner to the bottom right corner is stored in dp[m-1][n-1]
print(dp[m-1][n-1])
