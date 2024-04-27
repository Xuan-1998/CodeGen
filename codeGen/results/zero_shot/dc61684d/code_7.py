def dfs(node, visited, graph):
    visited[node] = True
    for neighbor in graph[node]:
        if not visited[neighbor]:
            dfs(neighbor, visited, graph)

def count_components(graph, n):
    visited = [False] * (n + 1)
    components = 0
    for i in range(1, n + 1):
        if not visited[i]:
            dfs(i, visited, graph)
            components += 1
    return components

# Read input
n, m = map(int, input().split())
graph = {i: [] for i in range(1, n + 1)}
for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

k = int(input())
experiments = [tuple(map(int, input().split())) for _ in range(k)]

# Perform experiments
for l, r in experiments:
    # Temporarily remove the edge
    graph[l].remove(r)
    graph[r].remove(l)

    # Count components
    components = count_components(graph, n)
    print(components)

    # Reconnect the edge
    graph[l].append(r)
    graph[r].append(l)
