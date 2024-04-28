def count_paths(K, N, arr):
    dp = [[[0] * (K+1) for _ in range(N)] for _ in range(N)]
    
    for i in range(N):
        dp[i][0][0] = 1
    
    for i in range(N):
        for j in range(N):
            if i == 0:
                dp[i][j][0] = 1
            elif j == 0:
                dp[i][j][0] = 1
            else:
                for k in range(min(j, i), -1, -1):
                    dp[i][j][k] += dp[i-1][k][0]
    
    return sum(sum(row) for row in dp[-1])
