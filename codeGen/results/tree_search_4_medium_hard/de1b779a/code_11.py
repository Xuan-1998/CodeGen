import sys

n, m, c0, d0 = map(int, input().split())
dp = [[0] * (m + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, m + 1):
        if i >= c0:
            dp[i][j] = max(dp[i][j], d0)
        if i >= ci[j - 1]:
            dp[i][j] = max(dp[i][j], di[j - 1] + dp[i - ci[j - 1]][j - 1])
        for k in range(j):
            if i >= ci[k]:
                dp[i][j] = max(dp[i][j], di[k] + dp[i - ci[k]][k])

print(max(dp[n]))
