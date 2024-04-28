n, m = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(m)]
k = int(input())
path = list(map(int, input().split()))

min_recompute = float('inf')
max_recompute = 0
current_vertex = path[0]
for vertex in path[1:]:
    if edges[vertex-1][1] != current_vertex:
        min_recompute = min(min_recompute, 1)
        max_recompute = max(max_recompute, 2)
    else:
        min_recompute = min(min_recompute, 1)
        max_recompute = max(max_recompute, 1)
    current_vertex = vertex
print(min_recompute, max_recompute)
