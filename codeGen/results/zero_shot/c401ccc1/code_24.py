import sys

def has_path(u, v):
    visited = set()
    queue = [(u, [u])]
    
    while queue:
        vertex, path = queue.pop(0)
        
        if vertex == v:
            return "YES"
        
        if vertex not in visited:
            visited.add(vertex)
            
            for neighbor in range(vertex + 1, min(vertex + (1 << 30), 2**31)):
                if (vertex & neighbor) == neighbor:
                    queue.append((neighbor, path + [neighbor]))
    
    return "NO"

q = int(sys.stdin.readline())
for _ in range(q):
    u, v = map(int, sys.stdin.readline().split())
    print(has_path(u, v))
