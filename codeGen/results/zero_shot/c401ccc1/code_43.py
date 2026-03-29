import sys
from collections import deque

def infinite_zoo(u, v):
    queue = deque([(0, False)])
    visited = set()
    
    while queue:
        current_vertex, is_power_of_two = queue.popleft()
        
        if current_vertex == u - 1 and not is_power_of_two:
            return "YES"
        if current_vertex >= v:
            return "NO"
        
        for next_vertex in range(current_vertex << 1, (current_vertex << 1) | 1):
            if next_vertex not in visited:
                queue.append((next_vertex, current_vertex & 1))
                visited.add(next_vertex)
    
    return "NO"

q = int(sys.stdin.readline())
for _ in range(q):
    u, v = map(int, sys.stdin.readline().split())
    print("YES" if infinite_zoo(u, v) else "NO")
