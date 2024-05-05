import sys

q = int(sys.stdin.readline())
graph = {}

for _ in range(q):
    u, v = map(int, sys.stdin.readline().split())
    graph[u] = set()
    graph[v] = set()
    if u & v:
        graph[u].add(v)
        graph[v].add(u)

def has_path(u, v):
    visited = set()

    def dfs(current):
        if current == v:
            return True
        if current in visited:
            return False
        visited.add(current)
        for neighbor in graph[current]:
            if dfs(neighbor):
                return True
        return False

    return dfs(u)

for _ in range(q):
    u, v = map(int, sys.stdin.readline().split())
    if has_path(u, v):
        print("YES")
    else:
        print("NO")
