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
min_recompute, max_recompute = 0, k - 1

for i in range(k - 1):
    min_recompute = max(min_recompute, len(graph.get(path[i], [])) - 1)
    max_recompute = min(max_recompute, len(graph.get(path[i], [])))

print(min_recompute, max_recompute)
