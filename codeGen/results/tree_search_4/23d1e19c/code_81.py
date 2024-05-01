def minmax_recomputations(n, m, edges, path):
    dp = [[float('inf'), float('-inf')] for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        if i in path:
            dp[i][0] = 0
            dp[i][1] = 0
        else:
            min_recomputation = float('inf')
            max_recomputation = float('-inf')
            for j in range(m):
                u, v = edges[j]
                if v == i:
                    min_recomputation = min(min_recomputation, dp[u][0] + 1)
                    max_recomputation = max(max_recomputation, dp[u][1] + 1)
            
            dp[i][0] = min_recomputation
            dp[i][1] = max_recomputation
    
    return dp[t][0], dp[t][1]
