from collections import defaultdict

def min_max_recomps(graph, s, t, path):
    n = len(graph)
    dist = {i: float('inf') for i in range(n)}
    recomp = defaultdict(int)

    # Initialize distances and recomputations
    dist[s] = 0
    recomp[s] = 0

    # Compute shortest distances and recomputations
    for u, v in graph:
        if dist[u] + 1 < dist[v]:
            dist[v] = dist[u] + 1
            recomp[v] = recomp[u] + 1

    # Compute minimum and maximum number of recomputations along the fixed path
    min_recomps = float('inf')
    max_recomps = 0
    for i in range(k-1):
        u, v = path[i], path[i+1]
        if dist[u] + 1 < dist[v]:
            min_recomps = min(min_recomps, recomp[u] + 1)
            max_recomps = max(max_recomps, recomp[u] + 1)

    return min_recomps, max_recomps

# Example usage:
graph = [(0, 1), (1, 2), (2, 3)]
s, t = 0, 3
path = [0, 1, 2]
print(min_max_recomps(graph, s, t, path))
