import sys

def dfs(node, parent, xor_sum):
    children = 0
    for neighbor in graph[node]:
        if neighbor != parent:
            children += 1
            xor_sum ^= nodes[neighbor]
            dfs(neighbor, node, xor_sum)

def solve(n, k, nodes, edges):
    graph = [[] for _ in range(n)]
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    components = {}
    for i in range(n):
        component_xor = 0
        dfs(i, -1, 0)
        if component_xor not in components:
            components[component_xor] = []
        components[component_xor].append(i)

    can_delete_edges = False
    for xor_sum, nodes_in_component in components.items():
        if len(nodes_in_component) > k:
            return "NO"

    return "YES"

n, k = map(int, sys.stdin.readline().split())
nodes = list(map(int, sys.stdin.readline().split()))
edges = []
for _ in range(n - 1):
    u, v = map(int, sys.stdin.readline().split())
    edges.append((u, v))

print(solve(n, k, nodes, edges))
