from collections import defaultdict

def max_vertices(n, m, T):
    graph = defaultdict(list)
    for _ in range(m):
        u, v, t = [int(i) for i in input().split()]
        graph[u].append((v, t))

    memo = {}
    def dfs(t, path):
        if (t, tuple(path)) in memo:
            return memo[(t, tuple(path))]
        if not path or path[-1] == n:
            return len(path)
        max_vertices = 0
        for v, edge_time in graph.get(1, []):
            if edge_time <= t:
                next_path = path + (v,)
                max_vertices = max(max_vertices, dfs(t - edge_time, next_path))
        memo[(t, tuple(path))] = max_vertices + 1
        return memo[(t, tuple(path))]

    return dfs(T, ())
