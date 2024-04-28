import heapq

def minmax_recomputations(n, m, edges, k, path):
    # Initialize graph and distance array
    graph = [[] for _ in range(n + 1)]
    dist = [float('inf')] * (n + 1)
    dist[0] = 0

    # Build graph and update distances
    for u, v in edges:
        graph[u].append(v)
        dist[v] = min(dist[v], dist[u] + 1)

    # Initialize priority queue with start vertex
    pq = [(0, 0)]
    visited = set()

    # Run Dijkstra's algorithm to find shortest path from s to t
    while pq:
        d, v = heapq.heappop(pq)
        if v not in visited:
            visited.add(v)
            for u in graph[v]:
                if u not in visited and d + 1 < dist[u]:
                    dist[u] = d + 1
                    heapq.heappush(pq, (d + 1, u))

    # Initialize minimum and maximum recomputations
    min_recomputations = float('inf')
    max_recomputations = -float('inf')

    # Update recomputations based on path
    for i in range(1, k):
        j = path[i]
        if dist[j] > dist[path[i - 1]]:
            min_recomputations = min(min_recomputations, 1)
            max_recomputations = max(max_recomputations, 1)
        else:
            min_recomputations = min(min_recomputations, 0)
            max_recomputations = max(max_recomputations, dist[j] - dist[path[i - 1]])

    # Print result
    print(min_recomputations, max_recomputations)

# Test case
n, m = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(m)]
k = int(input())
path = list(map(int, input().split()))
minmax_recomputations(n, m, edges, k, path)
