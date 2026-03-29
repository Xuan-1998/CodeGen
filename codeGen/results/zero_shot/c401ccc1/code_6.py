import sys

def bfs(u, v):
    visited = {u}
    queue = [u]
    while queue:
        node = queue.pop(0)
        if node == v:
            return "YES"
        for neighbor in range(node + 1, 2**30):  # iterate over all vertices
            if node & neighbor == neighbor:  # check if neighbor is reachable from node
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
    return "NO"

q = int(sys.stdin.readline())
for _ in range(q):
    u, v = map(int, sys.stdin.readline().split())
    print(bfs(u, v))
