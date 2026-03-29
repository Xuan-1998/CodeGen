def solve(n, m, T):
    # Step 1: Read the input edges and construct an adjacency list representation of the graph
    edges = []
    for _ in range(m):
        u, v, t = map(int, input().split())
        edges.append((u, v, t))

    # Step 2: Sort the edges by their traversal times (t)
    edges.sort(key=lambda x: x[2])

    # Step 3: Perform a topological sort on the graph
    visited = [False] * (n + 1)
    time_limit_reached = False

    for u, v, t in edges:
        if not visited[u]:
            dfs(u, visited, time_limit_reached)
        if time_limit_reached:
            break

    # Step 4: Find the maximum number of vertices that can be visited
    max_vertices = 0
    current_time = 0
    for i in range(1, n + 1):
        if visited[i]:
            current_time += 1
            if current_time > T:
                time_limit_reached = True
                break
        else:
            current_time = 0

    # Step 5: Print the result
    print(max_vertices)
    for i in range(1, max_vertices + 1):
        print(i, end=' ')
