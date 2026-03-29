import sys

n, m, c0, d0 = map(int, input().split())
dp = [[0] * (m + 1) for _ in range(n + 1)]

for i in range(m + 1):
    ai, bi, ci, di = map(int, input().split())
    dp[c0][i] = max(dp[c0][i], d0)

for i in range(1, n + 1):
    for j in range(m + 1):
        if i >= ci and j > 0:
            dp[i][j] = max(dp[i][j], dp[i - ci][j - 1] + di)
        elif i >= bi:
            dp[i][j] = max(dp[i][j], dp[i - bi][j] + di)

print(max(map(max, dp)))
