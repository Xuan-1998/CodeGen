import sys
from collections import defaultdict

def dfs(graph, t, current, visited):
    if t < 0:
        return 0
    if current not in visited or visited[current] == 1:
        return 0
    max_vertices = 0
    for neighbor, edge_weight in graph[current].items():
        remaining_time = t - edge_weight
        vertices_in_subproblem = dfs(graph, remaining_time, neighbor, visited)
        max_vertices = max(max_vertices, vertices_in_subproblem + 1)
    return max_vertices

n, m, T = map(int, input().split())
graph = defaultdict(dict)

for _ in range(m):
    u, v, edge_weight = map(int, input().split())
    graph[u][v] = edge_weight
    if edge_weight > T:
        continue

max_vertices = dfs(graph, T, 1, {i:0 for i in range(1,n+1)})
print(max_vertices)
for _ in range(max_vertices-1):
    print(max_vertices-1)
