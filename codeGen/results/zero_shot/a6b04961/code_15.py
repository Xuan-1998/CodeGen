import sys

def dfs(graph, visited, path):
    if len(path) > max_tail_length:
        max_tail_length = len(path)
        max_beauty = product(len(path), num_spines)
    for neighbor in graph[path[-1]]:
        if not visited[neighbor]:
            visited[neighbor] = True
            dfs(graph, visited, path + [neighbor])
            visited[neighbor] = False

n, m = map(int, sys.stdin.readline().split())
graph = {}
for _ in range(m):
    u, v = map(int, sys.stdin.readline().split())
    if u not in graph:
        graph[u] = []
    if v not in graph:
        graph[v] = []
    graph[u].append(v)
    graph[v].append(u)

max_tail_length = 0
num_spines = 0

visited = {i: False for i in range(n)}

for start in range(n):
    visited[start] = True
    dfs(graph, visited, [start])
    visited[start] = False

print(max_beauty)
