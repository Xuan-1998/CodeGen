from collections import defaultdict

def dfs(graph, node, visited):
    visited[node] = True
    for neighbor in graph[node]:
        if not visited[neighbor]:
            dfs(graph, neighbor, visited)

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
for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

k = int(input())
experiments = [tuple(map(int, input().split())) for _ in range(k)]

# Perform experiments
for li, ri in experiments:
    # Temporarily remove the edge by copying and modifying the adjacency list
    temp_graph = defaultdict(list, {node: neighbors[:] for node, neighbors in graph.items()})
    temp_graph[li].remove(ri)
    temp_graph[ri].remove(li)
    
    # Count the number of connected components with the edge removed
    print(count_components(temp_graph, n))

    # Edge is automatically reconnected for the next iteration, as we're working with a copy of the graph
