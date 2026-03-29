import sys
from collections import defaultdict, deque

def solve():
    n = int(sys.stdin.readline())
    graph = defaultdict(list)
    
    # Build the graph
    for _ in range(n-1):
        u, v = map(int, sys.stdin.readline().split())
        graph[u].append(v)

    # Find the root node with the minimum degree
    roots = []
    degrees = [0] * (n+1)
    for i in range(1, n+1):
        for neighbor in graph[i]:
            degrees[neighbor] += 1

    for i in range(n+1):
        if degrees[i] == 0:
            roots.append(i)

    # Find the minimum number of roads to be reversed
    reversed_edges = 0
    queue = deque(roots)
    
    while queue:
        node = queue.popleft()
        for neighbor in graph[node]:
            degrees[neighbor] -= 1
            if degrees[neighbor] == 0:
                queue.append(neighbor)

    # Count the minimum number of reversed edges
    for i in range(n+1):
        if degrees[i] > 0:
            reversed_edges += degrees[i]

    # Find all possible ways to choose the capital
    capitals = []
    visited = [False] * (n+1)
    
    def dfs(node, path):
        visited[node] = True
        for neighbor in graph[node]:
            if not visited[neighbor]:
                dfs(neighbor, path + [node])
        
    for root in roots:
        if not visited[root]:
            dfs(root, [root])

    # Print the results
    print(reversed_edges)
    for capital in capitals:
        print(' '.join(map(str, capital)))
