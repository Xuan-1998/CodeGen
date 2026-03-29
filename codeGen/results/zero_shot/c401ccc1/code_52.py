from collections import deque

def bfs(u, v):
    visited = set()
    queue = deque([(u, [u])])

    while queue:
        node, path = queue.popleft()

        if node == v:
            return "YES"

        for neighbor in range(2**30):
            if (node & neighbor) == neighbor and neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [neighbor]))

    return "NO"


q = int(input())

for _ in range(q):
    u, v = map(int, input().split())
    print("YES" if bfs(u, v) else "NO")
