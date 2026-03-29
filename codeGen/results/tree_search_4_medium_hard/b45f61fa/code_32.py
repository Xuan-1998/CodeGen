def minMult(n, p):
    dp = [[[0]*(n+1) for _ in range(n+1)] for _ in range(n+1)]
    
    for length in range(2, n+1):
        for i in range(n-length+1):
            j = i + length - 1
            dp[i][j][0] = float('inf')
            for k in range(i, j+1):
                cost_left = dp[i][k][0] + dp[k+1][j][0]
                if cost_left < dp[i][j][0]:
                    dp[i][j][0] = cost_left
    return dp[0][n-1][0]
