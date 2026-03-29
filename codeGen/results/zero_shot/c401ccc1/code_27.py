def zookeeper(u, v):
    # Perform DFS from vertex u to vertex v
    visited = set()
    stack = [(u, [])]

    while stack:
        (vertex, path) = stack.pop()
        if vertex == v:
            return "YES"  # Path found!
        if vertex not in visited:
            visited.add(vertex)
            for neighbor in [n for n in range(2**30) if vertex & n == n]:
                stack.append((neighbor, path + [vertex]))

    return "NO"  # No path found

q = int(input())
for _ in range(q):
    u, v = map(int, input().split())
    print(zookeeper(u, v))
