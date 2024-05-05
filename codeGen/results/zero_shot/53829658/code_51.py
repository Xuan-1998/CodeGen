import sys
from collections import defaultdict

def dfs(node, parent, depth, visited, rev_edges):
    visited.add(node)
    max_depth = depth
    for neighbor in graph[node]:
        if neighbor != parent:
            if neighbor not in visited:
                rev_edges[neighbor] = True
                max_depth = max(max_depth, dfs(neighbor, node, depth + 1, visited, rev_edges))
                rev_edges[neighbor] = False
            else:
                max_depth = max(max_depth, depth + 1)
    return max_depth

n = int(sys.stdin.readline())
graph = defaultdict(list)
for _ in range(n - 1):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)

visited = set()
rev_edges = {i: False for i in range(1, n + 1)}
max_depth = 0
capital = None

for node in range(1, n + 1):
    if node not in visited:
        dfs(node, -1, 0, visited, rev_edges)
        capital = node
        break

print(max_depth)
print(*[i for i in range(1, n + 1) if i != capital], sep=' ')
