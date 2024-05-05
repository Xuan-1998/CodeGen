import sys
from collections import defaultdict, deque

def read_input():
    n = int(sys.stdin.readline())
    graph = defaultdict(list)
    for _ in range(n-1):
        u, v = map(int, sys.stdin.readline().split())
        graph[u].append(v)
    return n, graph

def find_minimum_reversals_and_capitals(graph):
    # Step 1: Find the root of each connected component
    roots = {}
    for node in graph:
        visited = set()
        dfs(node, graph, visited, roots)
    
    # Step 2: Calculate the number of reversals needed to reach each capital from any other city
    min_reversals = float('inf')
    capitals = []
    for root in roots:
        reversals = 0
        visited = set()
        dfs(root, graph, visited, None)
        for node in graph:
            if node not in visited and node != root:
                reversals += len(visited)
        min_reversals = min(min_reversals, reversals)
        capitals.append([node for node in graph if node != root])
    
    return min_reversals, capitals

def dfs(node, graph, visited, roots):
    visited.add(node)
    if node not in roots:
        roots[node] = node
    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs(neighbor, graph, visited, roots)

def main():
    n, graph = read_input()
    min_reversals, capitals = find_minimum_reversals_and_capitals(graph)
    print(min_reversals)
    for capital in capitals:
        print(' '.join(map(str, capital)))

if __name__ == "__main__":
    main()
