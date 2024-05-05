from collections import deque

def bfs(u, v):
    queue = deque([(u, 0)])  # (vertex, distance)
    visited = {u}
    
    while queue:
        vertex, dist = queue.popleft()
        
        if vertex == v:
            return "YES"
        
        for neighbor in range(2**30):  # generate all possible neighbors
            if not (neighbor & vertex) or neighbor in visited:  # skip invalid edges
                continue
            
            if neighbor not in visited:
                queue.append((neighbor, dist + 1))
                visited.add(neighbor)
    
    return "NO"

q = int(input())
for _ in range(q):
    u, v = map(int, input().split())
    print("YES" if bfs(u, v) else "NO")
