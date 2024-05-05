def max_vertices(n, m, T):
    edges = []
    for _ in range(m):
        u, v, w = map(int, input().split())
        edges.append((u, v, w))

    dp = [[0] * (T + 1) for _ in range(n + 1)]
    
    for t in range(T + 1):
        dp[0][t] = 0

    for u, v, w in edges:
        for t in range(w - 1, T + 1):
            dp[v][t] = max(dp[v][t], dp[u][t - w] + 1)

    k = 0
    for i in range(n, 0, -1):
        if dp[i][T] > k:
            k = dp[i][T]
            print(i, end=' ')
    
    print()

max_vertices(int(input()), int(input()), int(input()))
