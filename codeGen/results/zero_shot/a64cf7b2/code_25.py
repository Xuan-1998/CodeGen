# Step 1: Read the input
n, m, T = map(int, input().split())
graph = {}
for _ in range(m):
    u, v, t = map(int, input().split())
    if u not in graph:
        graph[u] = []
    if v not in graph:
        graph[v] = []
    graph[u].append((v, t))
