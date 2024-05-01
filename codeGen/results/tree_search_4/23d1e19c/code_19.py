import sys

n, m = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(m)]
k = int(input())
path = list(map(int, input().split()))

dp = [[0] * (n + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    dp[i][i] = 0

for u, v in edges:
    for j in range(min(u, v), max(u, v) + 1):
        dp[u][v] = min(dp[u][v], dp[u][j] + 1)

min_recompute = float('inf')
max_recompute = 0

for i in range(1, k + 1):
    min_recompute = min(min_recompute, dp[path[i - 1]][path[i]])
    max_recompute = max(max_recompute, dp[path[i - 1]][path[i]])

print(min_recompute, max_recompute)
