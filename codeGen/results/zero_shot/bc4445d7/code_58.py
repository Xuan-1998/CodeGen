import sys
from collections import defaultdict

n = int(sys.stdin.readline())
edges = []
for _ in range(n - 1):
    u, v = map(int, sys.stdin.readline().split())
    edges.append((u, v))

m = int(sys.stdin.readline())
p = list(map(int, sys.stdin.readline().split()))
k = 1
for i in p:
    k *= i

tree = defaultdict(dict)
for u, v in edges:
    tree[u][v] = 1
    if u not in tree[v]:
        tree[v][u] = 1

visited = set()
dist_index = 0

def dfs(node, parent):
    global dist_index
    visited.add(node)
    for neighbor in tree[node]:
        if neighbor != parent:
            dfs(neighbor, node)
            dist_index += 1

dfs(1, None)

print(dist_index % (10**9 + 7))
