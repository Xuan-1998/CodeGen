from sys import stdin

# Read input grid size
m, n = map(int, stdin.readline().split())

# Initialize dp array with zeros
dp = [[0] * n for _ in range(m)]

# Fill dp array using nested loops
for i in range(m):
    for j in range(n):
        if i == 0 and j == 0:
            # Base case: top-left corner
            dp[i][j] = grid[i][j]
        elif i > 0:
            # Come from above
            dp[i][j] = min(dp[max(0, i-1)][j]) + grid[i][j]
        elif j > 0:
            # Come from left
            dp[i][j] = min(dp[i][max(0, j-1)]) + grid[i][j]

# Print the minimum sum of all numbers along the path
print(dp[m-1][n-1])
