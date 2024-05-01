import sys
from math import floor

n, m = map(int, input().split())

dp = [[0] * (m + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    dp[i][0] = 1
for j in range(1, m + 1):
    dp[0][j] = 1

for i in range(1, n + 1):
    for j in range(1, m + 1):
        if i < j:
            dp[i][j] = min(dp[i - 1][j], dp[i][j - 1])
        else:
            a = floor(i / j)
            b = floor(j / i)
            dp[i][j] = min(dp[i - 1][j] + a, dp[i][j - 1] + b)

print(dp[n][m])
