import sys
from collections import deque

q = int(input())
graph = {}

for _ in range(q):
    u, v = map(int, input().split())
    
    if u not in graph:
        graph[u] = set()
    if v not in graph:
        graph[v] = set()
        
    for i in range(u.bit_length()):
        mask = (1 << i)
        neighbor = u ^ mask
        graph[neighbor].add(v)

def bfs(vert):
    visited = set()
    queue = deque([vert])
    visited.add(vert)

    while queue:
        node = queue.popleft()

        for neighbor in graph.get(node, set()):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return len(visited) == 2**30

for _ in range(q):
    u, v = map(int, input().split())
    
    print("YES" if bfs(u) and (u & v) == v else "NO")
