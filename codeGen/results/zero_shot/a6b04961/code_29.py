def dfs(graph, node, visited, parent):
    # Mark the current node as visited
    visited[node] = True

    # Traverse neighbors
    for neighbor in graph[node]:
        if not visited[neighbor]:
            dfs(graph, neighbor, visited, node)
        elif neighbor != parent:
            # Found a spine! Update the maximum beauty
            global max_beaauty
            max_beaauty = max(max_beauty, len(visited) - 1)

    return

def find_max_beauty(graph):
    n, m = len(graph), len(graph[0])
    visited = [False] * (n + 1)
    max_beauty = 0
    for i in range(1, n + 1):
        if not visited[i]:
            dfs(graph, i, visited, -1)
    return max_beauty

n, m, edges = read_input()
graph = [[] for _ in range(n + 1)]
for u, v in edges:
    graph[u].append(v)
    graph[v].append(u)

max_beauty = find_max_beauty(graph)
print(max_beauty)
