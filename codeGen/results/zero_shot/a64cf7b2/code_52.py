import sys
from collections import deque

n, m, T = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    u, v, t = map(int, input().split())
    graph[u].append((v, t))

dp = [0] * (n + 1)
visited = [[False] * (T + 1) for _ in range(n + 1)]

def dfs(u):
    for v, t in graph[u]:
        if visited[v][t - dp[u]]: continue
        visited[v][t - dp[u]] = True
        dp[v] = max(dp[v], dp[u] + t)
        dfs(v)

dfs(1)
print(max(i for i in range(n+1) if dp[i] <= T))
for i in range(n+1):
    if dp[i] <= T:
        print(i, end=' ')
