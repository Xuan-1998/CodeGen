import sys

# Step 1: Read the input
n, m, T = map(int, sys.stdin.readline().split())
graph = {}
for _ in range(m):
    u, v, t = map(int, sys.stdin.readline().split())
    if u not in graph:
        graph[u] = []
    if v not in graph:
        graph[v] = []
    graph[u].append((v, t))

# Step 2: Define a function to perform DFS
def dfs(vertex, time_left, visited):
    max_vertices = 0
    vertices = []
    for neighbor, edge_time in graph.get(vertex, []):
        if time_left >= edge_time:
            new_time_left = time_left - edge_time
            new_visited = set(visited)
            new_visited.add(neighbor)
            result = dfs(neighbor, new_time_left, new_visited)
            if result[0] > max_vertices:
                max_vertices = result[0]
                vertices = result[1]
    return (max_vertices + 1, list(visited) + vertices)

# Step 3: Perform DFS from vertex 1 to vertex n
result = dfs(1, T, {1})
print(result[0])
print(' '.join(map(str, result[1])))
