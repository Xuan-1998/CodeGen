import sys

# Read input from stdin
n, m, c0, d0 = map(int, input().split())
dp = [[0] * (m + 1) for _ in range(n + 1)]
for i in range(m + 1):
    dp[0][i] = d0 if i == 0 else 0

# Fill the DP table
for i in range(1, n + 1):
    for j in range(1, m + 1):
        ai, bi, ci, di = map(int, input().split())
        if i >= ci:
            dp[i][j] = max(dp[i - ci][j - 1] + di, dp[i - ci][j] + d0)
        else:
            dp[i][j] = dp[i][j - 1] + d0

# Print the maximum profit
print(dp[n][m])
