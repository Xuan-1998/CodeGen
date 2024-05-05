import sys

n, m, c0, d0 = map(int, input().split())
dp = [[0] * (m + 1) for _ in range(n + 1)]

for j in range(m + 1):
    dp[0][j] = 0

for i in range(1, n + 1):
    for j in range(m + 1):
        if i >= c0:
            dp[i][j] = max(dp[max(0, i-c0)][min(j-1, m-1)], dp[i-1][0]) + d0
        else:
            dp[i][j] = dp[i-1][0]

print(max(dp[n]))
