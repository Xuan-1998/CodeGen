import sys
from collections import deque

n, m, T = map(int, input().split())
edges = []
for _ in range(m):
    u, v, t = map(int, input().split())
    edges.append((u, v, t))

visited = set()
queue = deque([(1, 0)]) # (vertex, time)
while queue:
    vertex, time = queue.popleft()
    if vertex == n and time <= T:
        max_visit = len(visited)
        break
    for edge in edges:
        u, v, t = edge
        if vertex == u and time + t <= T and v not in visited:
            visited.add(v)
            queue.append((v, time + t))

print(max_visit)

route = []
while (vertex, time) != (n, 0):
    for edge in edges:
        u, v, t = edge
        if vertex == u and time + t <= T:
            route.append(vertex)
            vertex = v
            time += t
            break

print(*route[::-1], sep='\n')
