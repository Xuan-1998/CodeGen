import sys

# Read input
n, m, T = map(int, sys.stdin.readline().split())
edges = []
for _ in range(m):
    u, v, t = map(int, sys.stdin.readline().split())
    edges.append((u, v, t))

# Build the graph
graph = {}
for edge in edges:
    if edge[0] not in graph:
        graph[edge[0]] = []
    if edge[1] not in graph:
        graph[edge[1]] = []
    graph[edge[0]].append((edge[1], edge[2]))

# Find the maximum number of vertices that can be visited within the time limit
visited = [False] * (n + 1)
max_vertices = 0
for i in range(1, n):
    if not visited[i]:
        max_vertices += 1
        for j in range(i + 1, n):
            if j not in graph:
                break
            for neighbor, time in graph[j]:
                if time <= T - sum(time for _, time in graph[neighbor]):
                    visited[j] = True
                    break

# Print the result
print(max_vertices)
for i in range(1, max_vertices + 1):
    print(i)
