import sys

n, m, T = map(int, sys.stdin.readline().split())
vertices = {}
for _ in range(m):
    u, v, t = map(int, sys.stdin.readline().split())
    if u not in vertices:
        vertices[u] = []
    if v not in vertices:
        vertices[v] = []
    vertices[u].append((v, t))

def dp(vertex, time, visited):
    if vertex == n:
        return 0
    if (vertex, time) in visited:
        return visited[(vertex, time)]
    
    max_vertices = 0
    for neighbor, t in vertices.get(vertex, []):
        if time + t <= T:
            max_vertices = max(max_vertices, dp(neighbor, time + t, visited | {(vertex, time): True}))
    
    visited.add((vertex, time))
    return max_vertices + 1

k = dp(1, 0, set())
print(k)

visited_vertices = []
vertex, time = n, T
while vertex != 1:
    for neighbor, t in vertices.get(vertex, []):
        if time + t <= T and dp(neighbor, time + t, set()) > len(visited_vertices):
            time += t
            vertex = neighbor
            visited_vertices.append(vertex)
visited_vertices.reverse()
print(*visited_vertices, sep='\n')
