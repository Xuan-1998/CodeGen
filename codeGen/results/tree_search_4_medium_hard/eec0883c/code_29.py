import sys
from collections import defaultdict

def dfs(u):
    visited.add(u)
    for v in graph[u]:
        if not visited.contains(v):
            w_v = weights[v]
            if w_v - w_u > 0:
                f = min(c, (w_v - w_u) // (c + 1))
                dp[v] += f
                dp[u] -= f
    return

n = int(input())
weights = [int(x) for x in input().split()]
graph = defaultdict(list)
for _ in range(n-1):
    u, v, c = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
    weights[v] += c

visited = set()
dp = [0] * (n+1)

dfs(1)

print(max(dp))
