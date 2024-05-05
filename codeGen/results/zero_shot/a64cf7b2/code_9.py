import sys

# Read input from stdin
n, m, T = map(int, sys.stdin.readline().split())
edges = []
for _ in range(m):
    u, v, t = map(int, sys.stdin.readline().split())
    edges.append((u, v, t))

# Topological sorting using Kahn's algorithm
in_degree = [0] * (n + 1)
graph = [[] for _ in range(n + 1)]

for u, v, t in edges:
    graph[u].append((v, t))
    in_degree[v] += 1

queue = [(0, 0)]  # Initialize queue with vertex 1 and time 0
top_sorted_vertices = []

while queue:
    time, vertex = queue.pop(0)
    top_sorted_vertices.append(vertex)

    for neighbor, edge_time in graph[vertex]:
        if time + edge_time <= T:
            queue.append((time + edge_time, neighbor))

# Calculate the maximum number of visited vertices
max_visited_vertices = 0

for i in range(len(top_sorted_vertices) - 1):
    max_visited_vertices += 1

print(max_visited_vertices)
print(*top_sorted_vertices[1:], sep='\n')
