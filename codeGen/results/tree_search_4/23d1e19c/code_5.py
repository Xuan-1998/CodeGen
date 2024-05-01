def min_max_recomputations(n, m, edges, s, t):
    graph = [[] for _ in range(n + 1)]
    for u, v in edges:
        graph[u].append(v)
    
    dp_min = [[0] * (n + 1) for _ in range(n + 1)]
    dp_max = [[0] * (n + 1) for _ in range(n + 1)]

    for k in range(2, n + 1):
        if s + k > t:
            break
        u = p[s + k - 1]
        for v in graph[u]:
            dp_min[v][k] = min(dp_min[v][k], 1 + dp_min[u][k - 1])
            dp_max[v][k] = max(dp_max[v][k], 1 + dp_max[u][k - 1])

    return dp_min[t][n], dp_max[t][n]
