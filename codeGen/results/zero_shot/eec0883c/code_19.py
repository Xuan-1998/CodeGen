import sys

def dfs(node, remaining_gasoline):
    if node == 'E':  # End node (destination city)
        return remaining_gasoline
    
    max_gasoline = 0
    for neighbor in graph[node]:
        edge_length = edges[neighbor][1]
        gas_left = min(remaining_gasoline, w[neighbor] - edge_length)
        max_gasoline = max(max_gasoline, dfs(neighbor, gas_left))
    
    return max_gasoline

n = int(sys.stdin.readline())
w = [int(x) for x in sys.stdin.readline().split()]
edges = {}
for _ in range(n-1):
    u, v, c = map(int, sys.stdin.readline().split())
    if u not in edges:
        edges[u] = []
    if v not in edges:
        edges[v] = []
    edges[u].append((v, c))
    edges[v].append((u, c))

max_gasoline = 0
for city in edges:
    max_gasoline = max(max_gasoline, dfs(city, w[city]))

print(max_gasoline)
