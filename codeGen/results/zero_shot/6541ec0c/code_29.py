import sys

def dfs(node, parent, xor_val):
    if parent != -1:
        xor_val ^= node_values[node]
    connected_components[0].append(xor_val)
    for neighbor in graph[node]:
        if neighbor != parent:
            dfs(neighbor, node, xor_val)

n, k = map(int, sys.stdin.readline().split())
node_values = list(map(int, sys.stdin.readline().split()))
graph = [[] for _ in range(n)]
for _ in range(n - 1):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

connected_components = [[], []]
node_values.sort()
xor_val = node_values[0]
dfs(0, -1, xor_val)
for comp in connected_components:
    if len(set(comp)) > 1:
        print("NO")
        sys.exit()

print("YES")
