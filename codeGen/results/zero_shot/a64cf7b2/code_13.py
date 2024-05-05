import heapq

n, m, T = map(int, sys.stdin.readline().split())
edges = []
for _ in range(m):
    u, v, t = map(int, sys.stdin.readline().split())
    edges.append((u, v, t))

graph = {}
for edge in edges:
    if edge[0] not in graph:
        graph[edge[0]] = []
    if edge[1] not in graph:
        graph[edge[1]] = []
    graph[edge[0]].append((edge[1], edge[2]))
    graph[edge[1]].append((edge[0], 0))  # reverse edge with zero weight

def dijkstra(graph, start, end):
    dist = {v: float('inf') for v in graph}
    dist[start] = 0
    pq = [(0, start)]
    while pq:
        d, u = heapq.heappop(pq)
        if d > dist[u]:
            continue
        for v, w in graph[u]:
            if w + d < dist[v]:
                dist[v] = w + d
                heapq.heappush(pq, (w + d, v))
    return dist[end]

vertices = list(range(1, n+1))
max_vertices = 0
time_left = T
while time_left > 0 and vertices:
    time_left -= dijkstra(graph, vertices[0], n)
    max_vertices += 1
    vertices.pop(0)

print(max_vertices)
for _ in range(max_vertices):
    print(vertices.pop(0))
