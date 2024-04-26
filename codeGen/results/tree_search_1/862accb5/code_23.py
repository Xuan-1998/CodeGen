import sys
from collections import defaultdict

sys.setrecursionlimit(210000)  # Increase recursion limit for large trees

def dfs(node, parent, graph, distances):
    for neighbor, length in graph[node]:
        if neighbor != parent:
            distances[neighbor] = distances[node] + length
            dfs(neighbor, node, graph, distances)

def main():
    # Read the number of towns (and roads)
    n = int(input().strip())

    # Initialize the graph
    graph = defaultdict(list)

    # Read the road descriptions
    for _ in range(n):
        u, v, l = map(int, input().split())
        graph[u].append((v, l))
        graph[v].append((u, l))

    # Step 1: Perform DFS to find the farthest node from an arbitrary root (node 1)
    distances = [0] * (n + 1)
    dfs(1, -1, graph, distances)

    # Find the farthest node from the root
    farthest_node = distances.index(max(distances))

    # Step 2: Perform DFS to find the diameter and record longest paths
    distances = [0] * (n + 1)
    dfs(farthest_node, -1, graph, distances)

    # Diameter is the maximum distance found
    diameter = max(distances)

    # Find the edge to remove (the one on the path with the maximum length)
    max_edge_length = 0
    for u in range(1, n + 1):
        for v, l in graph[u]:
            if distances[u] + l == distances[v] or distances[v] + l == distances[u]:
                max_edge_length = max(max_edge_length, l)

    # Output the minimum possible inconvenience (diameter - length of removed edge)
    print(diameter - max_edge_length)

if __name__ == "__main__":
    main()
