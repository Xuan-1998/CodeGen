code
from collections import defaultdict

def dfs(i, v, T):
    if i == n:
        return v + 1
    if (i, v, T) in memo:
        return memo[(i, v, T)]
    
    max_vertices = v
    for edge in edges:
        if edge[0] == i and T >= edge[2]:
            next_i, next_v, t = edge[1], v + 1, edge[2]
            T -= t
            max_vertices = max(max_vertices, dfs(next_i, next_v, T))
    
    memo[(i, v, T)] = max_vertices
    return max_vertices

n, m, T = map(int, input().split())
edges = []
memo = defaultdict(int)

for _ in range(m):
    u, v, t = map(int, input().split())
    edges.append((u, v, t))

print(dfs(1, 0, T))
