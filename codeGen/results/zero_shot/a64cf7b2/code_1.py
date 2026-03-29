n, m, T = map(int, input().split())
graph = {}
for _ in range(m):
    u, v, t = map(int, input().split())
    if u not in graph:
        graph[u] = []
    graph[u].append((v, t))

visited = set()
queue = []
for v in range(1, n+1):
    if v not in visited:
        queue.append(v)
while queue:
    v = queue.pop(0)
    visited.add(v)
    for u, t in graph.get(v, []):
        if u not in visited:
            queue.append(u)

max_vertices = 0
total_time = 0
for v in sorted(visited):
    if total_time + graph[v-1].get(v, 0)[2] > T:
        break
    max_vertices += 1
    total_time += graph[v-1].get(v, 0)[2]

print(max_vertices)
for v in sorted(visited):
    print(v)
