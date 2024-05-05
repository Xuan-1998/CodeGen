import sys

n, m, c0, d0 = map(int, input().split())
dp = [[0] * (m + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    dp[i][0] = max(dp[i - 1][0], d0)
for j in range(1, m + 1):
    dp[0][j] = d0
for j in range(1, m + 1):
        for i in range(1, n + 1):
            if i >= c0 and j > 0:
                dp[i][j] = max(dp[i - c0][j - 1] + d0, dp[i][j - 1])
            else:
                dp[i][j] = max(dp[i - c0][j], dp[i][j - 1])
print(dp[n][m])
