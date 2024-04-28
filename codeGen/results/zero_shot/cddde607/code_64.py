def solve(K, N, arr):
    dp = [[[0 for _ in range(K + 1)] for _ in range(N)] for _ in range(N)]
    
    for i in range(N):
        dp[i][0][0] = 1
    
    for i in range(N):
        for j in range(N):
            if i > 0:
                for k in range(min(j+1, K)+1):
                    dp[i][j][k] += dp[i-1][j][k]
            if j > 0:
                for k in range(min(i+1, K)+1):
                    dp[i][j][k] += dp[i][j-1][k]
    
    return dp[N-1][N-1][K]
