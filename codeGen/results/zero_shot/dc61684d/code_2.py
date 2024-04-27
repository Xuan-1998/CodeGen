from collections import defaultdict

def read_ints():
    return list(map(int, input().split()))

def remove_edge(graph, edge, edges):
    u, v = edges[edge - 1]
    graph[u].remove(v)
    graph[v].remove(u)

def add_edge(graph, edge, edges):
    u, v = edges[edge - 1]
    graph[u].append(v)
    graph[v].append(u)

def dfs(graph, start, visited):
    visited[start] = True
    for neighbor in graph[start]:
        if not visited[neighbor]:
            dfs(graph, neighbor, visited)

def count_components(n, graph):
    visited = [False] * (n + 1)
    components = 0
    for node in range(1, n + 1):
        if not visited[node]:
            dfs(graph, node, visited)
            components += 1
    return components

# Read input
n, m = read_ints()
edges = [tuple(read_ints()) for _ in range(m)]
k = int(input())
experiments = [tuple(read_ints()) for _ in range(k)]

# Build graph
graph = defaultdict(list)
for u, v in edges:
    graph[u].append(v)
    graph[v].append(u)

# Process experiments
for li, ri in experiments:
    remove_edge(graph, li, edges)
    print(count_components(n, graph))
    add_edge(graph, li, edges)
