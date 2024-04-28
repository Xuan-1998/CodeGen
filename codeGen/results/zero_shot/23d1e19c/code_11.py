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
path = list(map(int, input().split()))

min_recompute = float('inf')
max_recompute = 0

for i in range(1, k):
    for j in range(i-1, -1, -1):
        if path[j] not in graph:
            break
        max_recompute = i - j
        min_recompute = min(min_recompute, i - j)
