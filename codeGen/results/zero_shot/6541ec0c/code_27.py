import sys

def dfs(node, visited, stack):
    visited[node] = True
    for neighbor in edges[node]:
        if not visited[neighbor]:
            dfs(neighbor, visited, stack)
    stack.appendleft(node)

def get_component_id(node):
    # Implement this function later
    pass

def solve(n, k, nodes, edges):
    visited = [False] * n
    dfs_stack = []
    for i in range(n):
        if not visited[i]:
            dfs(i, visited, dfs_stack)

    xor_values = {}
    for node in dfs_stack:
        component_id = get_component_id(node)
        xor_value = 0
        for neighbor in edges[node]:
            xor_value ^= nodes[neighbor]
        xor_values[component_id] = xor_value

    count = 0
    for component_id, xor_value in xor_values.items():
        for node in dfs_stack:
            if get_component_id(node) == component_id and nodes[node] ^ xor_value != 0:
                count += 1
        if count > k:
            return "NO"

    return "YES"

n = int(sys.stdin.readline())
k = int(sys.stdin.readline())
nodes = list(map(int, sys.stdin.readline().split()))
edges = [[] for _ in range(n)]
for i in range(n-1):
    u, v = map(int, sys.stdin.readline().split())
    edges[u].append(v)
    edges[v].append(u)

print(solve(n, k, nodes, edges))
