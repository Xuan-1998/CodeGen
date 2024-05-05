===BEGIN CODE===
from sys import stdin, stdout
n, m, c0, d0 = map(int, stdin.readline().split())
dp = [0] * (n + 1)
for i in range(1, n + 1):
    if i <= c0:
        dp[i] = max(dp[i - 1], d0)
    for j in range(m):
        ai, bi, ci, di = map(int, stdin.readline().split())
        if i >= bi and i >= ci:
            pi = di - bi - ci
            dp[i] = max(dp[i], dp[bi + ci - 1] + pi)
stdout.write(str(max(dp)))
===END CODE===
