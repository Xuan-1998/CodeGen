import sys

def dfs(node, gas, visited):
    if visited[node]:
        return gas
    visited[node] = True
    max_gas = gas
    for neighbor in edges[node]:
        length = edge_lengths[neighbor]
        new_gas = min(gas, length)
        max_gas = max(max_gas, dfs(neighbor, new_gas, visited))
    return max_gas

n = int(sys.stdin.readline())
w = [int(x) for x in sys.stdin.readline().split()]
edges = {}
edge_lengths = {}

for i in range(n-1):
    u, v, c = map(int, sys.stdin.readline().split())
    if u not in edges:
        edges[u] = []
    if v not in edges:
        edges[v] = []
    edges[u].append(v)
    edge_lengths[(u, v)] = c
    edges[v].append(u)
    edge_lengths[(v, u)] = c

start_node = 0
visited = [False] * n
max_gas = dfs(start_node, w[start_node], visited)

print(max_gas)
