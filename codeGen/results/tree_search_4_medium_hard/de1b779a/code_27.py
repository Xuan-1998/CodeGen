import sys

n, m, c0, d0 = map(int, input().split())
dp = [[0 for _ in range(m+1)] for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(m+1):
        if i == 0:
            dp[i][j] = d0
        elif j == 0:
            dp[i][j] = c0
        else:
            not_used = dp[i-1][j]
            used = min(c0, c0 + sum(bi for _ in range(j)) - ci) + di
            dp[i][j] = max(not_used, used)

print(dp[n][m])
