from collections import deque

n, m = map(int, input().split())
graph = {}
for _ in range(m):
    u, v = map(int, input().split())
    if u not in graph:
        graph[u] = []
    if v not in graph:
        graph[v] = []
    graph[u].append(v)

k = int(input())
p = list(map(int, input().split()))

dp = [[float('inf'), 0] for _ in range(n + 1)]
for i in range(len(p) - 1):
    dp[p[i + 1]][p[:i + 1]] = min(dp[p[i + 1]][p[:i + 1]], dp[p[i]][p[:i]] + 1)
dp[t][p] = 0

print(min(dp[t]))
