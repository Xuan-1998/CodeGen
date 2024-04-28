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
for i in range(k - 1):
    for j in range(i + 1, k):
        min_len = float('inf')
        max_len = 0
        for x in range(path[i], path[j] + 1):
            if x not in graph:
                continue
            len_path = 0
            current = x
            while current != path[j]:
                len_path += 1
                current = next(vert for vert, neighbors in graph.items() if current in neighbors)
            min_len = min(min_len, len_path)
            max_len = max(max_len, len_path)
        min_recompute = min(min_recompute, min_len - 1)
        max_recompute = max(max_recompute, max_len - 1)
print(min_recompute, max_recompute)
