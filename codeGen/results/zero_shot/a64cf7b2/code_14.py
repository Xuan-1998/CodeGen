import sys
from collections import defaultdict

def topological_sorting():
    n, m, T = map(int, input().split())
    graph = defaultdict(list)
    
    for _ in range(m):
        u, v, t = map(int, input().split())
        graph[u].append((v, t))
    
    visited = [0] * (n + 1)
    queue = []
    for i in range(1, n + 1):
        if visited[i] == 0:
            queue.append(i)
    
    total_time = 0
    max_vertices = 0
    
    while queue:
        vertex = queue.pop(0)
        total_time += sum(t for v, t in graph[vertex])
        
        if total_time > T:
            return max_vertices
        
        visited[vertex] = 1
        max_vertices += 1
        
        for neighbor, t in graph[vertex]:
            visited[neighbor] -= 1
            if visited[neighbor] == 0:
                queue.append(neighbor)
    
    print(max_vertices)
    print(*range(1, max_vertices + 1), sep=' ')

topological_sorting()
