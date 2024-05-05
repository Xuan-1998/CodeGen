import sys

# Read input
n, m = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(m)]

dp = [[[0] * (n + 1) for _ in range(n + 1)] for _ in range(2)]

for i in range(1, n + 1):
    dp[0][i][i] = 1
    for j in range(m):
        u, v = edges[j]
        if i >= max(u, v):
            dp[1][max(u, v)][i] = max(dp[1][max(u, v)][i], dp[0][u][v] + 1)
