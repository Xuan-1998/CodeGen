import sys
from collections import deque

def solve(n, portals):
    # Create the graph and initialize distances
    graph = {i: [] for i in range(1, n+2)}
    for i in range(1, n+1):
        graph[i].append((portals[i-1], 1))
        graph[i].append((i+1, 1))

    # Run Dijkstra's algorithm
    dist = [float('inf')] * (n+2)
    dist[1] = 0
    queue = deque([1])
    while queue:
        node = queue.popleft()
        for neighbor, weight in graph[node]:
            if dist[neighbor] > dist[node] + weight:
                dist[neighbor] = dist[node] + weight
                queue.append(neighbor)

    # Return the distance from room 1 to room (n+1)
    return dist[n+1]

# Read input and run the solver
n = int(input())
portals = [int(x) for x in input().split()]
print(solve(n, portals))
