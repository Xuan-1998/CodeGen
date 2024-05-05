def min_destroyed_beacons():
    n, = map(int, input().split())
    dp = [[0]*(1000001) for _ in range(n+1)]
    
    for i in range(n):
        a, b, = map(int, input().split())
        dp[i][b] = b
    
    for i in range(1, n+1):
        for j in range(1, 1000001):
            for k in range(i-1, -1, -1):
                if j <= dp[k][min(b, j)]:
                    dp[i][j] = min(dp[i][j], dp[k][min(b, j)] + i-k)
    
    return dp[n][input().split()[0]]
