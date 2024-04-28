n, m = map(int, input().split())
graph = {}
for _ in range(m):
    u, v = map(int, input().split())
    if u not in graph:
        graph[u] = []
    if v not in graph:
        graph[v] = []
    graph[u].append(v)
s, t = map(int, input().split())
path_length = {i: float('inf') for i in range(1, n+1)}
for p in path_length:
    if p == s:
        path_length[p] = 0
    else:
        path_length[p] = float('inf')
min_recompute = float('inf')
max_recompute = 0
for p in path_length:
    for q in graph.get(p, []):
        path_length[q] = min(path_length[q], path_length[p]+1)
recompute_min = recompute_max = 0
for i in range(1, n+1):
    if path_length[i] > t:
        recompute_min = max(recompute_min, path_length[i]-t)
print(min_recompute, recompute_min)
