import sys

n, m, c0, d0 = map(int, input().split())
dp = [[0] * (d0 + 1) for _ in range(m)]

for i in range(m):
    a, b, c, d = map(int, input().split())
    for j in range(d0, c - 1, -1):
        dp[i][j] = max(dp[i-1][j], dp[i-1][j-c] + d)

print(max(dp[-1]))
