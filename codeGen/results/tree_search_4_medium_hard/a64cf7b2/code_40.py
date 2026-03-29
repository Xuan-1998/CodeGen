import sys

n, m, T = map(int, input().split())

dp = [[0] * (T + 1) for _ in range(n + 1)]

for _ in range(m):
    u, v, w = map(int, input().split())
    for t in range(T, w - 1, -1):
        dp[v][t] = max(dp[v][t], dp[u][t - w] + 1)

k = dp[n][T]
visited = []
t = T
while t > 0:
    visited.append(n)
    n -= (dp[n][t] - 1)
    t -= dp[n][t]
visited.reverse()

print(k, *visited, sep='\n')
