from collections import defaultdict

def dfs(graph, node, visited):
    visited[node] = True
    for neighbour in graph[node]:
        if not visited[neighbour]:
            dfs(graph, neighbour, visited)

def count_components(graph, n):
    visited = [False] * (n + 1)
    components = 0
    for i in range(1, n + 1):
        if not visited[i]:
            dfs(graph, i, visited)
            components += 1
    return components

# Read input
n, m = map(int, input().split())
graph = defaultdict(list)
edges = []

for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)
    edges.append((x, y))

k = int(input())

# Perform experiments
for _ in range(k):
    l, r = map(int, input().split())
    l -= 1  # Convert to 0-based index for the edge list
    graph[edges[l][0]].remove(edges[l][1])
    graph[edges[l][1]].remove(edges[l][0])

    # Count the number of connected components
    print(count_components(graph, n))

    # Reconnect the edge
    graph[edges[l][0]].append(edges[l][1])
    graph[edges[l][1]].append(edges[l][0])
