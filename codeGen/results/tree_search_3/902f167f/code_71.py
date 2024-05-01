# Read the dimensions of the rectangle
n, m = map(int, input().split())

# Initialize a 2D table to store the minimum number of squares required for each subproblem
dp = [[0] * (m + 1) for _ in range(n + 1)]

# Fill up the base cases
for i in range(n + 1):
    dp[i][0] = 0
for j in range(m + 1):
    dp[0][j] = 0

# Use memoization to fill up the rest of the table
for i in range(1, n + 1):
    for j in range(1, m + 1):
        if (i * i) <= j:
            dp[i][j] = min(dp[i - 1][j], dp[i][j - j]) + 1
        else:
            dp[i][j] = dp[i][j - 1] + 1

# Print the minimum number of squares required to tile the rectangle
print(dp[n][m])
