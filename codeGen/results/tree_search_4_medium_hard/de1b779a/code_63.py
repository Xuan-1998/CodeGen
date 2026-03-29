### BEGIN CODE ###
import sys

n, m, c0, d0 = map(int, input().split())
dp = [[0] * (m + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    dp[i][0] = max(0, dp[i - c0][1]) + d0

for j in range(1, m + 1):
    for i in range(cj[j], n + 1):
        dp[i][j] = max(dp[i - ci[j]][j - 1], dp[i - 1][0]) + di[j]

print(max(dp[n]))

### END CODE ###
