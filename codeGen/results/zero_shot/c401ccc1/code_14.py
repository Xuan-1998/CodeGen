import sys

def bfs(u, v):
    visited = set()
    queue = [u]

    while queue:
        node = queue.pop(0)
        if node == v:
            return "YES"
        for next_node in range(node + 1, 2**30): # assuming the maximum value is 2^30
            if (node & next_node) == next_node and next_node not in visited:
                queue.append(next_node)
                visited.add(next_node)
    return "NO"

q = int(sys.stdin.readline())
for _ in range(q):
    u, v = map(int, sys.stdin.readline().split())
    print(bfs(u, v))
