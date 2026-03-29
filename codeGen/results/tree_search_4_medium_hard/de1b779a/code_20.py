from collections import defaultdict

n, m, c0, d0 = map(int, input().split())
dp = [[0] * (m + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    dp[i][0] = d0 * min(c0 // i, n)

for j in range(1, m + 1):
    ai, bi, ci, di = map(int, input().split())
    for i in range(n, -1, -1):
        if i >= c0 // ci and dp[i - c0 // ci][j - 1] > dp[i][j]:
            dp[i][j] = dp[i - c0 // ci][j - 1] + di * min(c0 // ci, n)
        elif i >= bi and dp[i - bi][j]:
            dp[i][j] = dp[i - bi][j] + di
        else:
            dp[i][j] = dp[i][j]

print(dp[n][m])
