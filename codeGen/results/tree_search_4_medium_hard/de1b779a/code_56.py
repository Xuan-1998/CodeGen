import sys

n, m, c0, d0 = map(int, input().split())
dp = [[0] * (m + 1) for _ in range(n + 1)]

for j in range(1, m + 1):
    ai, bi, ci, di = map(int, input().split())
    for i in range(n + 1):
        dp[i][j] = max(
            (i < ci) * 0,
            (dp[max(i - ci, 0)][j - 1] + di) if i >= ci else 0,
            dp[i][j - 1]
        )

print(max(0, d0 + dp[n][m]))
