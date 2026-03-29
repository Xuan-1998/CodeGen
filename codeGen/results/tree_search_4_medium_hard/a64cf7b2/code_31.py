def max_vertices(n, m, T):
    edges = []
    for _ in range(m):
        u, v, t = map(int, input().split())
        edges.append((u-1, v-1, t))
    
    dp = [[0] * (T+1) for _ in range(n+1)]
    
    for i in range(1, n+1):
        for t in range(T, 0, -1):
            for u, v, w in edges:
                if i == v and t >= w:
                    dp[i][t] = max(dp[i][t], dp[u][t-w]+1)
    
    return dp[n][T]
