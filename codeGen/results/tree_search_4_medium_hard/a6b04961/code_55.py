def max_hedgehog_beauty(n, m, edges):
    dp = [[0] * (n + 1) for _ in range(n)]
    
    for i in range(2 * n):
        u, v = map(int, input().split())
        if dp[u][i]:
            dp[v][i + 1] = max(dp[v][i + 1], dp[u][i])
    
    return max(dp[i][j] for i in range(n) for j in range(2 * n))

n, m = map(int, input().split())
print(max_hedgehog_beauty(n, m, range(m)))
