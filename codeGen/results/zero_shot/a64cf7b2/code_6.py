import sys

def solve(n, m, T):
    # Read input
    edges = []
    for _ in range(m):
        u, v, t = map(int, sys.stdin.readline().split())
        edges.append((u, v, t))

    # Initialize adjacency list representation of the graph
    graph = {i: {} for i in range(1, n+1)}
    for u, v, t in edges:
        graph[u][v] = t

    # Perform topological sort on the graph
    visited = set()
    sorted_vertices = []
    for vertex in range(1, n+1):
        if vertex not in visited:
            stack = [vertex]
            while stack:
                curr_vertex = stack.pop()
                if curr_vertex not in visited:
                    visited.add(curr_vertex)
                    for neighbor in graph[curr_vertex]:
                        if neighbor not in visited:
                            stack.append(neighbor)

    # Dynamic programming to find the maximum number of vertices that can be visited
    dp = [0] * (n+1)
    dp[1] = 1
    for vertex in sorted_vertices:
        for neighbor in graph[vertex]:
            if neighbor == n:
                continue
            if dp[neighbor] < dp[vertex]:
                dp[neighbor] = min(dp[neighbor], dp[vertex] + 1)

    # Print the result: maximum number of vertices that can be visited and their indices
    k = max(range(2, n+1), key=lambda i: dp[i])
    print(k)
    for vertex in range(1, k+1):
        if dp[vertex] == dp[k]:
            print(vertex, end=' ')
