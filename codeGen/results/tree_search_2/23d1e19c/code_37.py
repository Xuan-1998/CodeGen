import heapq
def min_max_recomputations(n, m, edges, k, path):
    # Create an adjacency list representation of the graph
    graph = [[] for _ in range(n+1)]
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    # Initialize the minimum and maximum number of recomputations
    min_recomps = 0
    max_recomps = k - 1

    # Use a priority queue to maintain the shortest distance from each vertex to t
    pq = [(0, path[0])]  # (distance, vertex)
    while pq:
        dist, curr_vertex = heapq.heappop(pq)

        # If we've reached the last vertex in the fixed path, update the minimum and maximum number of recomputations
        if curr_vertex == path[-1]:
            min_recomps = min(min_recomps, dist)
            max_recomps = max(max_recomps, dist)
        else:
            # Calculate the distance from the current vertex to t
            for neighbor in graph[curr_vertex]:
                if neighbor not in path:
                    heapq.heappush(pq, (dist + 1, neighbor))

    return min_recomps, max_recomps

# Example usage:
n = int(input())
m = int(input())
edges = [(int(input()), int(input())) for _ in range(m)]
k = int(input())
path = [int(input()) for _ in range(k)]

min_recomps, max_recomps = min_max_recomputations(n, m, edges, k, path)

print(min_recomps, max_recomps)
