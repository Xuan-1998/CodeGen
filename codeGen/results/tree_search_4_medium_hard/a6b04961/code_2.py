import sys
from collections import defaultdict

n, m = map(int, input().split())
dp = [0] * (n + 1)
parent = [-1] * (n + 1)
graph = defaultdict(list)

for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

def dfs(node, length):
    if parent[node] == -1:
        for neighbor in graph[node]:
            if dp[neighbor] < dp[node] + 1:
                dp[neighbor] = dp[node] + 1
                parent[neighbor] = node
        return dp[node] * (length + 1)
    return dp[node]

for i in range(1, n):
    for node in graph[i]:
        if parent[node] == -1 and dfs(node, i) > dp[i]:
            dp[i] = dfs(node, i)

print(dp[-1])
