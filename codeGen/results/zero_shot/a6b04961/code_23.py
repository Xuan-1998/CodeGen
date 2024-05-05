import sys

def read_input():
    n, m = map(int, sys.stdin.readline().split())
    edges = []
    for _ in range(m):
        u, v = map(int, sys.stdin.readline().split())
        edges.append((u, v))
    return n, m, edges

def dfs(graph, node, visited, path):
    visited.add(node)
    path.append(node)
    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited, path)
    return path

def max_beauty(n, m, edges):
    # Create adjacency list
    graph = [[] for _ in range(n)]
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    # Find longest simple path (tail)
    visited = set()
    tail_path = []
    for node in range(n):
        if node not in visited:
            dfs(graph, node, visited, tail_path)

    # Remove edges from the tail
    remaining_edges = [(u, v) for u, v in edges if u not in tail_path or v not in tail_path]
    graph = [[] for _ in range(n)]
    for edge in remaining_edges:
        graph[edge[0]].append(edge[1])
        graph[edge[1]].append(edge[0])

    # Count spines
    spine_count = 0
    for node in range(n):
        for neighbor in graph[node]:
            if neighbor not in tail_path and (neighbor not in visited or node not in visited):
                spine_count += 1

    return len(tail_path) * spine_count

if __name__ == "__main__":
    n, m, edges = read_input()
    print(max_beauty(n, m, edges))
