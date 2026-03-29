from collections import deque

def infinite_zoo(u, v):
    # Prune the search space by finding the highest set bit in v
    mask = v & -v
    
    queue = deque([(u,)])
    visited = set()
    
    while queue:
        path = queue.popleft()
        
        # Check if we've reached v
        if path[-1] == v:
            return "YES"
        
        for neighbor in [(path[-1] | mask), (path[-1] & ~mask)]:
            if neighbor not in visited:
                queue.append(path + [neighbor])
                visited.add(neighbor)
    
    return "NO"

q = int(input())
for _ in range(q):
    u, v = map(int, input().split())
    print(infinite_zoo(u, v))
