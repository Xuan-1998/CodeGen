import sys

def solve(n, k, edges):
    # Create a graph using an adjacency list representation
    graph = [[] for _ in range(n)]
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    # Perform DFS to identify connected components
    visited = [False] * n
    component_values = []
    for node in range(n):
        if not visited[node]:
            component = []
            dfs(node, graph, visited, component)
            component_values.append(get_component_xor(component))

    # Check if the bitwise XOR is the same for all connected components
    xor_values = set(component_values)
    return "YES" if len(xor_values) == 1 else "NO"


def dfs(node, graph, visited, component):
    visited[node] = True
    component.append(node)
    for neighbor in graph[node]:
        if not visited[neighbor]:
            dfs(neighbor, graph, visited, component)


def get_component_xor(component):
    value = 0
    for node in component:
        value ^= a[node]
    return value


# Read input data from stdin
n, k = map(int, sys.stdin.readline().split())
a = list(map(int, sys.stdin.readline().split()))
edges = []
for _ in range(n-1):
    u, v = map(int, sys.stdin.readline().split())
    edges.append((u, v))

# Print the solution to stdout
print(solve(n, k, edges))
