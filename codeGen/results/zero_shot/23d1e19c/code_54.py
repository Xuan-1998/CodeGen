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

current_vertex = path[0]
for i in range(1, k):
    if path[i-1] not in graph or path[i] not in graph[path[i-1]]:
        min_recompute = min(min_recompute, len(graph) - i)
        max_recompute = max(max_recompute, len(graph) - (i-1))

print(min_recompute, max_recompute)
