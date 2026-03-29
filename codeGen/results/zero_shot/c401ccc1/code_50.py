graph = {}
for _ in range(int(input())):
    u, v = map(int, input().split())
    graph[u] = {v for v in range(2**30) if (u & v) == u}

def query(u, v):
    visited = set()
    stack = [u]
    while stack:
        vertex = stack.pop()
        if vertex == v:
            return "YES"
        for neighbor in graph.get(vertex, set()):
            if (vertex & neighbor) == vertex and neighbor not in visited:
                stack.append(neighbor)
                visited.add(neighbor)
    return "NO"

q = int(input())
for _ in range(q):
    u, v = map(int, input().split())
    print(query(u, v))
