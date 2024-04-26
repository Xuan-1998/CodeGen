import sys
from collections import defaultdict

def dfs(graph, node, parent, visited, cycle_edges):
    visited[node] = True
    for neighbor, length in graph[node]:
        if not visited[neighbor]:
            cycle_edges = dfs(graph, neighbor, node, visited, cycle_edges)
        elif neighbor != parent:
            # Found a cycle, update the maximum inconvenience edge in this cycle
            cycle_edges = max(cycle_edges, (length, node, neighbor))
    return cycle_edges

def find_min_inconvenience(n, roads):
    graph = defaultdict(list)
    for u, v, l in roads:
        graph[u].append((v, l))
        graph[v].append((u, l))

    visited = [False] * (n + 1)
    max_inconvenience_edge = (0, -1, -1)  # (length, node1, node2)

    # Run DFS from every unvisited node
    for node in range(1, n + 1):
        if not visited[node]:
            max_inconvenience_edge = dfs(graph, node, -1, visited, max_inconvenience_edge)

    return max_inconvenience_edge[0]

def main():
    n = int(input().strip())
    roads = [tuple(map(int, input().split())) for _ in range(n)]
    result = find_min_inconvenience(n, roads)
    print(result)

if __name__ == "__main__":
    main()
