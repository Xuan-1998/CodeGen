import sys
from collections import defaultdict

n, m, T = map(int, input().split())
edges = defaultdict(list)

for _ in range(m):
    u, v, t = map(int, input().split())
    edges[u].append((v, t))

dp = [[0] * (T + 1) for _ in range(n + 1)]

def dfs(i, t):
    if dp[i][t]:
        return dp[i][t]
    
    dp[i][t] = 1
    for j, edge_t in edges[i]:
        if t - edge_t >= 0:
            dp[i][t] = max(dp[i][t], dfs(j, t - edge_t) + 1)
    
    return dp[i][t]

print(dfs(1, T))
