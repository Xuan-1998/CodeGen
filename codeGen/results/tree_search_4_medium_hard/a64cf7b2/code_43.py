def max_vertices(n, m, T):
    edges = []
    for _ in range(m):
        u, v, w = map(int, input().split())
        edges.append((u, v, w))

    dp = [[0] * (T + 1) for _ in range(n + 1)]

    for t in range(T + 1):
        for i in range(1, n + 1):
            if not edges or all(j != i for _, j, _ in edges):
                dp[i][t] = 1
            else:
                for u, v, w in edges:
                    if i == u and t >= w:
                        dp[i][t] = max(dp[i][t], dp[v][t - w] + 1)

    return dp[1][T]

n, m, T = map(int, input().split())
print(max_vertices(n, m, T))
