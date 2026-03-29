def solve():
    n = int(input())
    
    # Initialize a list for tree edges
    tree_edges = [[] for _ in range(n+1)]
    
    # Read all roads (edges) and add them to the tree edges
    for i in range(1, n):
        u, v = map(int, input().split())
        tree_edges[u].append(v)
        tree_edges[v].append(u)
    
    # Find the minimum height of a vertex
    min_height = float('inf')
    capital_cities = []
    for i in range(1, n+1):
        visited = [False] * (n + 1)
        stack = [(i, 0)]  # (vertex, height)
        while stack:
            u, h = stack.pop()
            if not visited[u]:
                visited[u] = True
                for v in tree_edges[u]:
                    if not visited[v]:
                        stack.append((v, h + 1))
                min_height = min(min_height, h)
        capital_cities.append([i - 1 for i in range(1, n+1) if visited[i-1]])
    
    # Find the minimum number of roads to be reversed
    min_reversed = float('inf')
    for cities in capital_cities:
        reversed_edges = 0
        visited = [False] * (n + 1)
        stack = [(cities[0], 0)]  # (vertex, height)
        while stack:
            u, h = stack.pop()
            if not visited[u]:
                visited[u] = True
                for v in tree_edges[u]:
                    if not visited[v]:
                        stack.append((v, h + 1))
                    elif h < min_height - 1:
                        reversed_edges += 1
        min_reversed = min(min_reversed, reversed_edges)
    
    # Print the result
    print(min_reversed)
    for cities in capital_cities:
        print(' '.join(map(str, cities)))
