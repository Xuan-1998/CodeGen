n, m = map(int, input().split())
graph = {}
for _ in range(m):
    u, v = map(int, input().split())
    if u not in graph:
        graph[u] = []
    if v not in graph:
        graph[v] = []
    graph[u].append(v)
p = list(map(int, input().split()))
min_recompute = 0
max_recompute = float('inf')
for i in range(1, len(p)):
    u = p[i-1]
    v = p[i]
    if v not in graph[u]:
        min_recompute += 1
    while v not in graph:
        v = [w for w in graph[u] if w != v][0]
        min_recompute += 1
    max_recompute = min(max_recompute, len(graph[u]) - 1)
print(min_recompute, max_recompute)
