import sys

n, m, c0, d0 = map(int, input().split())
dp = [0] * (n + 1)
max_profit = 0

for _ in range(m):
    ai, bi, ci, di = map(int, input().split())
    for i in range(n, -1, -1):
        if i >= bi and i >= ci:
            dp[i] = max(dp[i], dp[i-bi] + di)
            if i >= c0:
                dp[i] = max(dp[i], dp[i-c0] + d0)

print(max(dp))
