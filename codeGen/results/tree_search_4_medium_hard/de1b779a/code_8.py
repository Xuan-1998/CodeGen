import sys

n, m, c0, d0 = map(int, input().split())
dp = [[0] * (m + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    dp[i][0] = dp[i - 1][0] + d0
for j in range(1, m + 1):
    dp[0][j] = dp[0][j - 1] + c0

for i in range(1, n + 1):
    for j in range(1, m + 1):
        if j <= i // (c0 + c[i - 1]):
            dp[i][j] = max(dp[i][j], dp[i - c0 - c[j - 1]][j - 1] + d[j] - b[j])
        else:
            dp[i][j] = dp[i][j - 1]

print(dp[n][m])
