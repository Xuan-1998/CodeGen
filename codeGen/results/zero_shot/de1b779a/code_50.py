import sys

n, m, c0, d0 = map(int, sys.stdin.readline().split())

dp = [0] * (m + 1)
for _ in range(m):
    a, b, c, d = map(int, sys.stdin.readline().split())
    for i in range(min(n, a), -1, -1):
        dp[i] = max(dp[i], dp[max(0, i-b)] + d)

print(max(dp))
