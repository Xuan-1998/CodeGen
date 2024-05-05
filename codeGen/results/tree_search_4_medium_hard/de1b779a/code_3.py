import sys

n, m, c0, d0 = map(int, input().split())
dp = [[0] * (m + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(m + 1):
        if j == 0:
            dp[i][j] = d0 * min(i // c0, n // c0) - c0 * min(i // c0, n // c0)
        else:
            ai, bi, ci, di = map(int, input().split())
            dp[i][j] = max(dp[i - 1][j], dp[i - (i // ci)][j - 1] + di - bi)

print(max(0, dp[n][m]))
