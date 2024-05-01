def min_max_recomputations(graph, path):
    n = len(graph)
    f = [float('inf')] * (n + 1)
    f[0] = 0

    for i in range(n - 1):
        v = path[i]
        for j in range(v + 1, n + 1):
            if graph[v][j - 1]:
                f[j] = min(f[j], 1 + f[v])

    return [f[n], f[n]]
