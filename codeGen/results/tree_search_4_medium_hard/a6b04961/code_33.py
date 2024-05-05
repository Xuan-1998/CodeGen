import sys
from collections import defaultdict

n, m = map(int, input().split())
graph = defaultdict(list)
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

dp = [0] * (n + 1)
count = [0] * (n + 1)

def dfs(i):
    if dp[i]:
        return dp[i]
    
    count[i] = len(graph[i])
    for j in graph[i]:
        if i < j:
            count[i] -= dfs(j)
    
    dp[i] = max(dp[i], count[i] + (i > 0))
    return dp[i]

print(max(dfs(i) for i in range(1, n + 1)))
