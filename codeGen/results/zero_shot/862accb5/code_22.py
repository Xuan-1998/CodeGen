import sys

def dfs(graph, node, parent, visited, edges):
    visited[node] = True
    for neighbor, length in graph[node]:
        if not visited[neighbor]:
            edges.append((node, neighbor, length))
            if dfs(graph, neighbor, node, visited, edges):
                return True
        elif neighbor != parent:
            # Found a cycle
            edges.append((node, neighbor, length))
            return True
    return False

def find_cycle(graph, n):
    visited = [False] * (n + 1)
    for i in range(1, n + 1):
        if not visited[i]:
            edges = []
            if dfs(graph, i, -1, visited, edges):
                return edges
    return []

def calculate_inconvenience(graph, n, cycle_edges):
    # TODO: Implement the calculation of all possible inconveniences
    # and return the minimum inconvenience.
    pass

def main():
    n = int(sys.stdin.readline().strip())
    graph = [[] for _ in range(n + 1)]
    for _ in range(n):
        u, v, l = map(int, sys.stdin.readline().strip().split())
        graph[u].append((v, l))
        graph[v].append((u, l))

    cycle_edges = find_cycle(graph, n)
    min_inconvenience = calculate_inconvenience(graph, n, cycle_edges)
    print(min_inconvenience)

if __name__ == "__main__":
    main()
