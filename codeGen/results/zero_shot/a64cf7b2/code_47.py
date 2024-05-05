import heapq

n, m, T = map(int, input().split())
edges = []
for _ in range(m):
    u, v, t = map(int, input().split())
    edges.append((u, v, t))

visited = set()
pq = [(0, 1)]
while pq:
    time, vertex = heapq.heappop(pq)
    if vertex == n:
        k = len(visited)
        break
    if time <= T and vertex not in visited:
        visited.add(vertex)
        for u, v, t in edges:
            if u == vertex:
                heapq.heappush(pq, (time + t, v))

print(k)
print(*visited, sep='\n')
