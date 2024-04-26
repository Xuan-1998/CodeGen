import sys

def dfs(graph, visited, node):
    visited.add(node)
    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs(graph, visited, neighbor)

n = int(sys.stdin.readline())
graph = {}
for i in range(n):
    p = int(sys.stdin.readline()) - 1
    if p not in graph:
        graph[p] = []
    while True:
        parent = (i + 1) % n
        if parent == 0:
            break
        graph[p].append(parent - 1)
        p = parent

trees = 0
visited = set()
for node in graph:
    if node not in visited:
        dfs(graph, visited, node)
        trees += 1

print(trees)

