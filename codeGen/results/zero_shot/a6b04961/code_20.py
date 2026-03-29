import sys
from collections import deque, defaultdict

def read_input():
    n, m = map(int, sys.stdin.readline().split())
    graph = defaultdict(list)
    for _ in range(m):
        u, v = map(int, sys.stdin.readline().split())
        graph[u].append(v)
        graph[v].append(u)
    return n, m, graph

def dfs(graph, start, visited, parent):
    for neighbor in graph[start]:
        if neighbor not in visited:
            visited.add(neighbor)
            parent[neighbor] = start
            dfs(graph, neighbor, visited, parent)

def max_hedgehog_beauty(n, m, graph):
    # Step 1: Perform DFS to find all connected components (CCs) in the graph
    visited = set()
    parent = {}
    for i in range(1, n+1):
        if i not in visited:
            dfs(graph, i, visited, parent)
    
    # Step 2: Sort CCs by their sizes and store them in a list
    cc_sizes = []
    temp_parent = {i: None for i in range(1, n+1)}
    for node in sorted(parent):
        if node not in visited:
            size = 0
            while node != None:
                node = parent[node]
                size += 1
            cc_sizes.append(size)
    
    # Step 3: Calculate the maximum possible beauty of a hedgehog
    max_beauty = 0
    for i, (size1, size2) in enumerate(zip(cc_sizes[:-1], cc_sizes[1:])):
        if size1 * size2 > max_beauty:
            max_beauty = size1 * size2
    
    return max_beauty

n, m, graph = read_input()
print(max_hedgehog_beauty(n, m, graph))
