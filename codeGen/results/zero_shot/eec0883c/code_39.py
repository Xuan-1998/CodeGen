import sys

def dfs(u, w_u, v, c):
    if u == v:
        return w_u - c
    if visited[u]:
        return -1  # Nut runs out of gasoline
    visited[u] = True
    return max(dfs(next_node, w_next, v, c) for next_node, w_next in graph[u])

n, *w = map(int, sys.stdin.readline().split())
graph = {}
visited = {i: False for i in range(1, n+1)}
for _ in range(n-1):
    u, v, c = map(int, sys.stdin.readline().split())
    if u not in graph:
        graph[u] = []
    if v not in graph:
        graph[v] = []
    graph[u].append((v, c))
    graph[v].append((u, c))

print(max(dfs(1, w[0], n, 0), key=lambda x: x) + w[-1])
