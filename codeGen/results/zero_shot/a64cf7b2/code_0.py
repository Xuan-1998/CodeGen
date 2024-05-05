def max_vertices(n, m, T):
    edges = []
    for _ in range(m):
        u, v, t = map(int, input().split())
        edges.append((u, v, t))

    dp = [[0] * (T + 1) for _ in range(n + 1)]
    visited = [False] * (n + 1)

    for u, v, t in edges:
        dp[v][t] = max(dp[v][t], dp[u][t - 1] + 1)
        visited[v] = True

    k = 0
    route = []
    for i in range(T, -1, -1):
        if visited[n]:
            k += 1
            route.append(n)
            n -= 1

    print(k)
    print(*route, sep=' ')
