import sys

n, m, T = map(int, sys.stdin.readline().split())
edges = []
for _ in range(m):
    u, v, t = map(int, sys.stdin.readline().split())
    edges.append((u, v, t))

graph = [[] for _ in range(n + 1)]
for u, v, t in edges:
    graph[u].append((v, t))

dp = [0] * (n + 1)
for i in range(1, n):
    dp[i] = T

for u in range(n):
    for v, t in graph[u]:
        if dp[v] < dp[u] - t:
            dp[v] = dp[u] - t

k = 0
path = []
for i in range(n, 0, -1):
    if dp[i] > 0:
        k += 1
        path.append(i)
print(k)
print(' '.join(map(str, path)))
