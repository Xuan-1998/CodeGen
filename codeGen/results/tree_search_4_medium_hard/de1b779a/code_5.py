import sys

# Read input
n, m, c0, d0 = map(int, input().split())
dp = [0] * (n + 1)
for _ in range(m):
    ai, bi, ci, di = map(int, input().split())

# Fill dp array
for i in range(1, n + 1):
    if i < c0:
        dp[i] = d0
    else:
        dp[i] = max(dp[i], dp[min(i - 1, c0)] + di)
        for j in range(m):
            if i >= ci[j]:
                dp[i] = max(dp[i], dp[i - ci[j]] + di[j])
