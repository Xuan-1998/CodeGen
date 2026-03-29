import heapq
from collections import defaultdict

# Read input
n, m = map(int, input().split())
graph = defaultdict(list)

for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

# Initialize variables
beauty = 0
tail = []
spines = []

# Start DFS from each vertex and find the maximum beauty
for i in range(1, n+1):
    visited = [False] * (n+1)
    heapq.heapify([(0, i)])
    parent = [-1] * (n+1)

    while heapq:
        length, vertex = heapq.heappop()
        if not visited[vertex]:
            visited[vertex] = True
            if len(tail) > 0 and tail[-1] == vertex - 1:
                beauty += 1
            for neighbor in graph[vertex]:
                if not visited[neighbor]:
                    parent[neighbor] = vertex
                    heapq.heappush((length+1, neighbor))

    # Reconstruct the longest path from the root to each leaf node
    current = i
    while True:
        tail.append(current)
        if parent[current] == -1:
            break
        current = parent[current]

# Calculate the number of spines
for vertex in range(1, n+1):
    if vertex not in tail and any(neighbor not in tail for neighbor in graph[vertex]):
        beauty += 1

print(beauty)
