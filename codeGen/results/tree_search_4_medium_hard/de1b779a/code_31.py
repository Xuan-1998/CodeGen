import sys

n, m, c0, d0 = map(int, input().split())
dp = [[0] * (m + 1) for _ in range(n + 1)]
memo = {}

for i in range(1, n + 1):
    ai, bi, ci, di = map(int, input().split())
    for j in range(m + 1):
        if i < c0:
            dp[i][j] = max(dp[i][j - 1], di)
        elif j == 0:
            dp[i][j] = d0
        else:
            if (i, j) not in memo:
                memo[(i, j)] = max(
                    bi + dp[i - ci][max(0, j - 1)],
                    dp[i][j - 1]
                )
            dp[i][j] = memo[(i, j)]

print(dp[n][m])
