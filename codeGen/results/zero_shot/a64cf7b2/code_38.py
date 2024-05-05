import sys
from collections import defaultdict

def dfs(graph, visited, current, time_left):
    if time_left < 0:
        return 0
    
    visited.add(current)
    max_vertices = 1
    
    for neighbor, weight in graph[current]:
        if neighbor not in visited:
            max_vertices = max(max_vertices, 1 + dfs(graph, visited, neighbor, time_left - weight))
    
    return max_vertices

def max_vertices(T):
    n, m = map(int, input().split())
    graph = defaultdict(list)
    
    for _ in range(m):
        u, v, t = map(int, input().split())
        graph[u].append((v, t))
    
    visited = set()
    max_visited = 0
    
    for vertex in range(1, n+1):
        if vertex not in visited:
            visited.clear()
            time_left = T
            max_visited = max(max_visited, dfs(graph, visited, 1, time_left))
    
    return max_visited

print(max_vertices(int(input())))
