import sys

def dfs(vertex, parent):
    visited.add(vertex)
    bitwise_and = vertex
    for neighbor in graph[vertex]:
        if neighbor == parent:
            continue
        if bitwise_and & neighbor != neighbor:
            return False
        if dfs(neighbor, vertex):
            return True
    return False

q = int(sys.stdin.readline())
graph = {}
visited = set()
for _ in range(q):
    u, v = map(int, sys.stdin.readline().split())
    graph[u] = [v & u]
    print("YES" if dfs(v, None) else "NO")
