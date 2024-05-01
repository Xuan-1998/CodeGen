def min_max_recomputations():
    n, m = map(int, input().split())
    graph = [[] for _ in range(n + 1)]
    for _ in range(m):
        u, v = map(int, input().split())
        graph[u].append(v)
    k = int(input())
    path = list(map(int, input().split()))
    
    dp = [[float('inf')] * (n + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        dp[i][i] = 0
    
    for i in range(n - 1, -1, -1):
        for j in range(i + 1, n + 1):
            if j in graph[i]:
                dp[i][j] = min(dp[i][j], dp[i][path[k-1]] + (k - 1))
    
    return min(dp[0][n]), max(dp[0][n])
