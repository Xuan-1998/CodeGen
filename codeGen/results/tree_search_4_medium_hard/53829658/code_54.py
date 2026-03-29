from collections import defaultdict

def treeland_capital():
    n = int(input())
    graph = defaultdict(list)
    
    # Read edges from stdin
    for _ in range(n-1):
        u, v = map(int, input().split())
        graph[u].append(v)

    # Calculate in-degrees of all cities
    in_degree = {i: 0 for i in range(1, n+1)}
    for city, neighbors in graph.items():
        for neighbor in neighbors:
            in_degree[neighbor] += 1

    # Find the optimal capital (city with maximum in-degree)
    max_in_degree = max(in_degree.values())
    capitals = [city for city, degree in in_degree.items() if degree == max_in_degree]

    # Calculate the minimum number of reversed roads
    min_reversed_roads = sum(in_degree.values()) - len(capitals)

    print(min_reversed_roads)
    print(' '.join(map(str, capitals)))

treeland_capital()
