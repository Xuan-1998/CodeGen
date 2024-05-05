import sys

n, m, c0, d0 = map(int, input().split())
dp = [[0] * (m + 1) for _ in range(n + 1)]

for j in range(m):
    ai, bi, ci, di = map(int, input().split())

dp[0][j] = 0
dp[i][0] = d0 * min(c0 // bi, n / ci) for i in range(1, n + 1)

for i in range(1, n + 1):
    for j in range(1, m + 1):
        if ai[j - 1] > 0 and i >= bi:
            dp[i][j] = max(dp[i - bi][j - 1] + di, d0 * min(c0 // bi, n / ci))
        else:
            dp[i][j] = dp[i][j - 1]

print(dp[n][m])
