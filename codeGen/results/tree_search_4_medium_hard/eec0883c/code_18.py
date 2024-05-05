def gas_station(w, c):
    n = len(w)
    jmax = max(w)
    cmax = max(c)
    
    dp = [[[0]* (cmax+1) for _ in range(jmax+1)] for _ in range(n)]
    
    for i in range(1, n):
        for j in range(jmax+1):
            for c_edge in range(cmax+1):
                if j < w[i-1]:
                    dp[i][j][c_edge] = 0
                else:
                    for k in range(w[i-1], -1, -1):
                        if j-k >= w[i-1]:
                            dp[i][j][c_edge] = max(dp[i][j-k][min(c[k-1], c_edge)], dp[i-1][j-k-c_edge][w[i-2]])
    
    return dp[n-1][w[-1]][0]
