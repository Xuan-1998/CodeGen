from collections import defaultdict

def find_capital(n, roads):
    # Create an adjacency list to represent the directed tree
    graph = defaultdict(list)
    for si, ti in roads:
        graph[si].append(ti)

    # Initialize the in-degree of each city to 0
    in_degree = [0] * (n + 1)

    # Calculate the in-degree of each city using the adjacency list
    for i in range(1, n + 1):
        for j in graph[i]:
            in_degree[j] += 1

    # Find the maximum in-degree, which corresponds to the optimal capital city
    max_in_degree = max(in_degree[1:])

    # Initialize a set to keep track of visited cities during DFS
    visited = set()

    # Perform DFS starting from each city with maximum in-degree (capital) to find all possible capital cities
    capital_cities = []
    for i in range(1, n + 1):
        if in_degree[i] == max_in_degree and i not in visited:
            visited.add(i)
            capital_cities.append(i)

    # Calculate the minimum number of roads that need to be reversed
    min_reversed_edges = sum(in_degree[1:] - [max_in_degree] * len(capital_cities))

    return min_reversed_edges, ' '.join(map(str, capital_cities))
