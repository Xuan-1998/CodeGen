import heapq
n, m, T = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    u, v, t = map(int, input().split())
    graph[u].append((v, t))

visited = [0] * (n + 1)
max_vertices = 0
route = []
heapq.heapify([(0, 1)])
while heapq:
    time, node = heapq.heappop()
    if visited[node] == 2:
        continue
    if time > T:
        break
    if node == n:
        max_vertices = max(max_vertices, len(route))
        for i in route:
            print(i)
        exit()
    visited[node] = 2
    for neighbor, edge_time in graph[node]:
        heapq.heappush((time + edge_time, neighbor))
