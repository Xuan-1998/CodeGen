import sys
from collections import defaultdict, deque

def solve():
    n, m, T = map(int, sys.stdin.readline().split())
    
    graph = defaultdict(list)
    for _ in range(m):
        u, v, t = map(int, sys.stdin.readline().split())
        graph[u].append((v, t))
    
    visited = [False] * (n + 1)
    distance = [0] * (n + 1)
    parent = [-1] * (n + 1)
    
    queue = deque([(1, T)])
    while queue:
        vertex, time_left = queue.popleft()
        if visited[vertex]:
            continue
        
        visited[vertex] = True
        distance[vertex] = time_left
        
        for neighbor, edge_time in graph[vertex]:
            if not visited[neighbor]:
                new_time_left = time_left - edge_time
                if new_time_left > 0:
                    queue.append((neighbor, new_time_left))
                    parent[neighbor] = vertex
    
    max_vertices = 0
    current_vertex = n
    path = []
    
    while current_vertex != 1:
        path.append(current_vertex)
        current_vertex = parent[current_vertex]
        max_vertices += 1
    
    path.append(1)
    path.reverse()
    
    print(max_vertices, *path, sep='\n')

if __name__ == "__main__":
    solve()
