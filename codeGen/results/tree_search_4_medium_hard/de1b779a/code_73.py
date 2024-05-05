import sys

# Input variables
n, m, c0, d0 = map(int, input().split())
dp = [[[-1 for _ in range(m + 1)] for _ in range(n + 1)] for _ in range(m + 1)]

# Initialize base cases
for i in range(m + 1):
    dp[0][i][0] = c0

for j in range(m + 1):
    dp[n][j][0] = d0

# Fill up the DP array
for i in range(1, n + 1):
    for j in range(1, m + 1):
        if i >= c0:
            dp[i][j][0] = max(dp[i][j][0], d0)
        else:
            dp[i][j][0] = 0

        for k in range(1, min(i // c0, j) + 1):
            dp[i][j][k] = max(dp[i][j][k-1], di[j-1] + dp[i-ci[j]][j-1][k-1])

# Print the maximum profit
print(max(dp[n][m]))
