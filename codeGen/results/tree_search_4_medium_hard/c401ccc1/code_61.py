from collections import deque

def zookeeper_queries():
    q = int(input())
    visited = set()
    memo = {}
    
    for _ in range(q):
        u, v = map(int, input().split())
        
        if (u, v) not in memo:
            memo[(u, v)] = bfs(u, v)
            
        print('YES' if memo[(u, v)][v] else 'NO')

def bfs(start, end):
    queue = deque([(start, [start])])
    visited = set()
    
    while queue:
        vertex, path = queue.popleft()
        
        if vertex == end:
            return {end: True}
            
        for neighbor in range(30):  # assuming 2^30 is the maximum number of vertices
            if (vertex & neighbor) and neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [neighbor]))
                
    return {}

zookeeper_queries()
