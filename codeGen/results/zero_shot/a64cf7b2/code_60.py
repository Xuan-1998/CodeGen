import sys

def dfs(graph, current_vertex, time_limit, max_vertices):
    if current_vertex == n:
        return max_vertices + 1
    for neighbor, edge_weight in graph[current_vertex]:
        if time_limit >= edge_weight and neighbor not in visited:
            visited.add(neighbor)
            new_time_limit = time_limit - edge_weight
            new_max_vertices = dfs(graph, neighbor, new_time_limit, max_vertices + 1)
            if new_max_vertices > max_vertices:
                max_vertices = new_max_vertices
    return max_vertices

n, m, T = map(int, sys.stdin.readline().split())
graph = {}
visited = set()

for _ in range(m):
    u, v, t = map(int, sys.stdin.readline().split())
    graph.setdefault(u, []).append((v, t))
    graph.setdefault(v, []).append((u, t))

max_vertices = 0
dfs(graph, 1, T, max_vertices)
print(max_vertices)

for vertex in visited:
    print(vertex)
