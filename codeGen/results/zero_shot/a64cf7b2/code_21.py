import sys

def solve():
    n, m, T = map(int, sys.stdin.readline().split())
    edges = []
    for _ in range(m):
        u, v, t = map(int, sys.stdin.readline().split())
        edges.append((u, v, t))

    # Sort the edges by time
    edges.sort(key=lambda x: x[2])

    # Initialize the graph and visited set
    graph = [[] for _ in range(n+1)]
    visited = set()

    def dfs(vertex, time):
        if vertex > n:
            return 0
        if vertex == n:
            return 1
        if time + edges[vertex-1][2] > T:
            return 0
        if vertex in visited:
            return 0
        visited.add(vertex)
        max_vertices = 0
        for neighbor, t in graph[vertex]:
            max_vertices = max(max_vertices, dfs(neighbor, time+t))
        visited.remove(vertex)
        return max_vertices + 1

    # Start the DFS from vertex 1
    max_vertices = dfs(1, 0)

    # Print the result
    print(max_vertices)
    for i in range(max_vertices-1):
        print(graph[i+1][0], end=' ')
    print()

solve()
