from collections import defaultdict

def read_input():
    n, m = map(int, input().split())
    edges = [tuple(map(int, input().split())) for _ in range(m)]
    k = int(input())
    experiments = [tuple(map(int, input().split())) for _ in range(k)]
    return n, m, edges, k, experiments

def build_graph(n, edges):
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    return graph

def dfs(graph, node, visited):
    visited[node] = True
    for neighbor in graph[node]:
        if not visited[neighbor]:
            dfs(graph, neighbor, visited)

def connected_components(graph, n):
    visited = [False] * (n + 1)
    components = 0
    for node in range(1, n + 1):
        if not visited[node]:
            components += 1
            dfs(graph, node, visited)
    return components

def perform_experiments(n, edges, experiments):
    for l, r in experiments:
        # Temporarily remove the edge
        graph = build_graph(n, edges[:l-1] + edges[r:])
        # Count the connected components
        components = connected_components(graph, n)
        # Output the result
        print(components)

def main():
    n, m, edges, k, experiments = read_input()
    perform_experiments(n, edges, experiments)

if __name__ == "__main__":
    main()
