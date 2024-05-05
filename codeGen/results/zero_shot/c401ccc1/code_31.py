import sys

def bfs(u, v):
    queue = [u]
    visited = {u}
    while queue:
        node = queue.pop(0)
        if node == v:
            return "YES"
        for neighbor in range(node+1, 2**30):  # iterate over all possible neighbors
            if (node & neighbor) == neighbor and neighbor not in visited:
                queue.append(neighbor)
                visited.add(neighbor)
    return "NO"

q = int(sys.stdin.readline())
for _ in range(q):
    u, v = map(int, sys.stdin.readline().split())
    print(bfs(u, v))
