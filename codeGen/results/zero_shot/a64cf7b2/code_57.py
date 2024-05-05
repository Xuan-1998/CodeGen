import sys

def dfs(graph, visited, vertex):
    if not visited[vertex]:
        visited[vertex] = True
        for neighbor in graph[vertex]:
            dfs(graph, visited, neighbor)

def bfs(graph, visited, queue, T):
    while queue:
        vertex = queue.popleft()
        if not visited[vertex]:
            visited[vertex] = True
            for neighbor in graph[vertex]:
                if neighbor == n:  # Check if we've reached the last vertex (n)
                    return T
                queue.append(neighbor)

n, m, T = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    u, v, t = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)  # Since this is a DAG, we only need to store one edge per vertex pair.

visited = [False] * (n + 1)

# Sort the edges based on their weights
edges = []
for i in range(1, n + 1):
    for neighbor in graph[i]:
        edges.append((i, neighbor))
edges.sort(key=lambda x: x[2])

max_vertices = 0
queue = [1]
visited[1] = True

while queue:
    bfs(graph, visited, queue, T)
    max_vertices += 1
    if max_vertices == n:  # Check if we've reached the last vertex (n)
        break

print(max_vertices)

# Print the indices of vertices that can be visited on the route from vertex 1 to vertex n
visited = [False] * (n + 1)
queue = [1]
while queue:
    vertex = queue.pop(0)
    if not visited[vertex]:
        print(vertex, end=' ')
        for neighbor in graph[vertex]:
            if not visited[neighbor]:
                queue.append(neighbor)
        visited[vertex] = True
