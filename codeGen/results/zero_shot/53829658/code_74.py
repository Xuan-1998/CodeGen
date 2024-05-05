from collections import defaultdict

def min_edges_to_reverse(n, roads):
    graph = defaultdict(list)
    for si, ti in roads:
        graph[si].append(ti)

    # Initialize a dictionary to store the minimum number of edges to reverse
    # from each city as the capital
    min_reversals = {i: 0 for i in range(1, n+1)}

    # Perform DFS from each city as the capital
    for city in range(1, n+1):
        visited = set()
        stack = [(city, 0)]  # (city, reversals)
        while stack:
            city, reversals = stack.pop()
            if city not in visited:
                visited.add(city)
                for neighbor in graph[city]:
                    if neighbor not in visited:
                        stack.append((neighbor, reversals + 1))
                    else:
                        min_reversals[neighbor] = min(min_reversals.get(neighbor, float('inf')), reversals)

    # Find the city with the minimum number of edges to be reversed
    capital = min(min_reversals, key=min_reversals.get)
    print(min_reversals[capital])  # Output: minimum number of edges to be reversed

    # Print all possible ways to choose the capital (i.e., sequence of indexes)
    capitals = sorted(range(1, n+1), key=lambda x: min_reversals[x])
    print(*capitals, sep='\n')  # Output: sequence of index numbers
