from collections import deque

def bfs(u, v):
    visited = set()
    queue = deque([(u, [u])])
    
    while queue:
        vertex, path = queue.popleft()
        
        if vertex == v:
            return "YES"
        
        for next_vertex in range(2**30):  # Iterate over all vertices
            if (vertex & next_vertex) and next_vertex not in visited:
                visited.add(next_vertex)
                queue.append((next_vertex, path + [next_vertex]))
    
    return "NO"

for u, v in queries:
    print(bfs(u, v))
