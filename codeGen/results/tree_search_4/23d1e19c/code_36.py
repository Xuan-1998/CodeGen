===BEGIN CODE===
import sys

n, m = map(int, input().split())
dp = [[(0, 0)] * (n + 1) for _ in range(n + 1)]

for i in range(2, n):
    dp[i][s - 1] = (0, 0)

for j in range(s, t + 1):
    if p[j - 1] == i:
        dp[i][j] = (min(dp[i - 1][j - 1][0] + 1, dp[p[j - 1]][j - 1][0]), max(dp[i - 1][j - 1][1], dp[p[j - 1]][j - 1][1]))
    else:
        dp[i][j] = (dp[i - 1][j - 1][0], dp[i - 1][j - 1][1])

print(dp[n][t])
===END CODE===
