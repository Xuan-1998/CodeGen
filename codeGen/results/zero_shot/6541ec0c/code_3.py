import sys

def dfs(node, parent, xor_val):
    global visited
    visited[node] = True
    total_xor = xor_val
    for neighbor in graph[node]:
        if neighbor != parent:
            if not visited[neighbor]:
                total_xor ^= dfs(neighbor, node, total_xor)
            else:
                total_xor ^= visited_nodes[neighbor]
    return total_xor

visited = [False] * (n + 1)
graph = [[] for _ in range(n + 1)]
visited_nodes = [0] * (n + 1)

# Read input and build graph
n, k = map(int, sys.stdin.readline().split())
for _ in range(k):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

# Perform DFS on each connected component
connected_components = []
for i in range(1, n + 1):
    if not visited[i]:
        xor_val = dfs(i, -1, 0)
        connected_components.append((xor_val, [i]))

# Check if all nodes in a connected component have the same XOR value
same_xor = True
for component in connected_components:
    xor_val, nodes = component
    if len(set(xor_val ^ visited_nodes[node] for node in nodes)) > 1:
        same_xor = False
        break

print("YES" if same_xor else "NO")
