from collections import deque

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)

k = int(input())
path = list(map(int, input().split()))

dp_min = [float('inf')] * (n + 1)
dp_max = [-float('inf')] * (n + 1)

for i in range(n):
    if path[i] != -1:
        dp_min[path[i]] = 0
        dp_max[path[i]] = 0

for i in range(1, n + 1):
    for v in graph[i]:
        if v != -1:
            dp_min[v] = min(dp_min[v], dp_min[i] + 1)
            dp_max[v] = max(dp_max[v], dp_max[i] + 1)

print(dp_max[path[-1]], dp_min[path[-1]])
