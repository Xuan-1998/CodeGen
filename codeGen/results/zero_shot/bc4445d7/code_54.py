# Solution starts here
import heapq
from collections import defaultdict

def find_max_distribution_index():
    n = int(input())
    parent = list(range(n))
    edges = []
    for i in range(n - 1):
        u, v = map(int, input().split())
        parent[v] = u
        edges.append((u, v))

    m = int(input())
    primes = list(map(int, input().split()))

    graph = defaultdict(dict)
    for edge in edges:
        u, v = edge
        graph[u][v] = 1

    max_distribution_index = 0

    while True:
        # Step 1: Find a node with the maximum out-degree.
        max_out_degree_node = None
        max_out_degree = -1
        for node in range(n):
            out_degree = sum(1 for neighbor in graph[node] if parent[neighbor] == node)
            if out_degree > max_out_degree:
                max_out_degree = out_degree
                max_out_degree_node = node

        # Step 2: Find the maximum out-degree edge.
        max_out_degree_edge = None
        max_out_degree = -1
        for neighbor in graph[max_out_degree_node]:
            out_degree = sum(1 for grandchild in graph[neighbor] if parent[grandchild] == max_out_degree_node)
            if out_degree > max_out_degree:
                max_out_degree = out_degree
                max_out_degree_edge = (max_out_degree_node, neighbor)

        # Step 3: Update the maximum distribution index.
        max_distribution_index += max_out_degree

        # Step 4: Update the parent array and the graph.
        for child in graph[max_out_degree_edge[1]]:
            parent[child] = max_out_degree_edge[0]
            del graph[max_out_degree_edge[1]][child]
            if not graph[max_out_degree_edge[1]]:
                del graph[max_out_degree_edge[1]]
        del graph[max_out_degree_edge[0]][max_out_degree_edge[1]]

    return max_distribution_index % (10**9 + 7)

print(find_max_distribution_index())
