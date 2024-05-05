import sys

n, m, c0, d0 = map(int, input().split())
dp = [[0] * (m + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, m + 1):
        ai, bi, ci, di = map(int, input().split())
        
        if ai <= i and bi <= c0:
            dp[i][j] = max(dp[i][j], di + dp[i-ci][j-1])
            dp[i][j] = max(dp[i][j], d0)
        else:
            dp[i][j] = max(dp[i][j], d0)

print(dp[n][m])
