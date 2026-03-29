import sys

def dfs(node, parent, visited, xor_values):
    # Mark node as visited
    visited.add(node)
    
    # Initialize XOR value for this connected component
    xor_value = 0
    
    for child in graph[node]:
        if child != parent:
            if child not in visited:
                xor_value ^= dfs(child, node, visited, xor_values)[1]
            else:
                xor_value ^= xor_values[child-1]
    
    return xor_value, visited

n, k = map(int, sys.stdin.readline().split())
values = list(map(int, sys.stdin.readline().split()))
graph = [[] for _ in range(n+1)]

for _ in range(n-1):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

visited = set()
xor_values = [0] * (n+1)

# Perform DFS
root = 1
while root:
    xor_value, visited = dfs(root, -1, visited, xor_values)
    if len(visited) == 1:  # Root node with no children
        break
    root = None

print("YES" if all(xor_values[i] == xor_values[0] for i in range(1, n+1)) else "NO")
