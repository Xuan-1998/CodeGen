import sys

n, m, c0, d0 = map(int, sys.stdin.readline().split())

dp = [[0] * (n + 1) for _ in range(m + 1)]

for i in range(1, m + 1):
    ai, bi, ci, di = map(int, sys.stdin.readline().split())
    for j in range(1, n + 1):
        dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - (ci - bi)] + di)

print(max(dp[-1]))
