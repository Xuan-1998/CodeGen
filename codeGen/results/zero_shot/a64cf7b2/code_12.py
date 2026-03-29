import heapq

n, m, T = map(int, input().split())
edges = []
for _ in range(m):
    u, v, t = map(int, input().split())
    edges.append((u, v, t))

edges.sort(key=lambda x: x[2])

visited = set()
heap = [(0, 1)]  # Initialize the heap with vertex 1 and weight 0

while heap:
    t, v = heapq.heappop(heap)
    if v not in visited:
        visited.add(v)
        for u, _, w in edges:
            if u == v:  # Explore the edges
                heapq.heappush(heap, (t + w, u))

max_vertices = len(visited)

print(max_vertices)

# Print the indices of vertices that can be visited on the route from vertex 1 to vertex n
for v in sorted(visited):
    print(v)
