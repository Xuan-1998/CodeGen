import heapq

def min_max_recomputations(graph, fixed_path):
    # Precompute all shortest paths from each vertex in the graph to t
    shortest_paths = {}
    for i in range(len(fixed_path) - 1):
        u, v = fixed_path[i], fixed_path[i + 1]
        dist_u_to_v = float('inf')
        for edge in graph:
            if edge[0] == u and edge[1] == v:
                dist_u_to_v = min(dist_u_to_v, edge[2])
        shortest_paths[u] = dist_u_to_v
        shortest_paths[v] = dist_u_to_v

    # Initialize variables to track minimum and maximum recomputations
    min_recomputations = 0
    max_recomputations = 0

    for i in range(1, len(fixed_path)):
        u, v = fixed_path[i - 1], fixed_path[i]
        if shortest_paths[u] != shortest_paths[v]:
            # Recomputation needed!
            min_recomputations += 1
            max_recomputations = max(max_recomputations, min_recomputations)

    return min_recomputations, max_recomputations

# Example usage:
graph = [(1, 2, 3), (2, 3, 4), (3, 4, 5)]  # Add more edges as needed
fixed_path = [1, 2, 3, 4]

min_recomps, max_recomps = min_max_recomputations(graph, fixed_path)
print(min_recomps, max_recomps)
