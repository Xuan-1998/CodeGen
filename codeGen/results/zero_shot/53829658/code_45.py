from collections import defaultdict

def find_centers_and_minimum_edges():
    n = int(input())
    graph = defaultdict(list)
    for _ in range(n-1):
        u, v = map(int, input().split())
        graph[u].append(v)

    max_degrees = [0] * (n+1)
    centers = []
    for node, children in graph.items():
        max_degrees[node] = len(children)
        if max_degrees[node] > 0:
            centers.append(node)

    minimum_edges_to_reverse = float('inf')
    possible_capitals = []
    for capital in centers:
        subtree_max_degree = 0
        for node, children in graph.items():
            if children[0] == capital:  # This is a node in the subtree rooted at capital
                max_degree_in_subtree = len(children) - 1
                subtree_max_degree += max_degree_in_subtree
        minimum_edges_to_reverse = min(minimum_edges_to_reverse, n - 2 - subtree_max_degree)
        possible_capitals.append(centers.index(capital))

    print(minimum_edges_to_reverse)
    print(' '.join(map(str, possible_capitals)))

find_centers_and_minimum_edges()
