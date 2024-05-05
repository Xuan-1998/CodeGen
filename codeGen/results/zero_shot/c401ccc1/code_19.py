edges = []
for u in range(2**30):
    for v in range(u+1, 2**30):
        if u & v == v:
            edges.append((u, v))

def dfs(graph, u, v):
    visited = set()
    stack = [(u, [u])]
    while stack:
        node, path = stack.pop(0)
        if node == v:
            return "YES"
        if node not in visited:
            visited.add(node)
            for neighbor in graph.get(node, []):
                stack.append((neighbor, path + [neighbor]))
    return "NO"

q = int(input())
for _ in range(q):
    u, v = map(int, input().split())
    print("YES" if dfs({u: edges[u], v: edges[v]}.get(u, []), u, v) else "NO")
