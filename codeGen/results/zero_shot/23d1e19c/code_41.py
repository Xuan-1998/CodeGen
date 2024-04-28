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
k = int(input())
path = list(map(int, input().split()))

min_recompute = float('inf')
max_recompute = 0

current_vertex = s
recompute_count = 0

for vertex in path:
    if vertex != current_vertex:
        recompute_count += 1
    current_vertex = vertex

print(recompute_count, recompute_count)
