import sys

def process_input():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    edges = []
    for _ in range(n-1):
        u, v = map(int, input().split())
        edges.append((u, v))
    return n, k, a, edges

def dfs(graph, node, visited, parent, component_values):
    visited[node] = True
    component_values[0] ^= a[node]
    for neighbor in graph[node]:
        if neighbor != parent:
            if not visited[neighbor]:
                dfs(graph, neighbor, visited, node, component_values)
            else:
                component_values[0] ^= a[neighbor]

def solve(n, k, a, edges):
    graph = [[] for _ in range(n)]
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    
    visited = [False] * n
    component_values = [0]
    for node in range(n):
        if not visited[node]:
            dfs(graph, node, visited, -1, component_values)

    xor_values = set()
    for i in range(len(component_values) - 1):
        xor_values.add(component_values[i])

    return "YES" if len(xor_values) == 1 else "NO"

n, k, a, edges = process_input()
print(solve(n, k, a, edges))
