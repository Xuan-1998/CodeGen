# Define the grid size (assuming it's a square)
n = int(input())

# Initialize the dp table with zeros
dp = [[0] * n for _ in range(n)]

# Fill up the dp table using tabulation
for i in range(n):
    for j in range(n):
        # Calculate the minimum sum considering all elements in the first i-1 rows and last j-1 columns, plus the value at row i and column j
        dp[i][j] = min(dp[i-1][k] if i > 0 else 0 for k in range(j)) + grid[i][j]

# Find the minimum sum of a falling path with non-zero shifts
min_sum = float('inf')
for j in range(n):
    min_sum = min(min_sum, dp[-1][j])

print(min_sum)
