def steadyTables(N, M):
    MOD = 10**9 + 7

    dp = [[0] * (M + 1) for _ in range(N + 1)]
    
    # Base case: when all rows are filled
    for j in range(M + 1):
        dp[N][j] = 1

    # Fill up the table
    for i in range(N - 1, -1, -1):
        for j in range(M + 1):
            # If the last row sum is less than or equal to M, we can choose a new row sum from 0 to M
            dp[i][j] = (dp[i][j] + dp[i + 1][min(j, M)]) % MOD
            
            # If the last row sum is greater than M, we need to reduce the current row sum by some amount to make it less than or equal to M
            if j > M:
                for k in range(1, M + 1):
                    dp[i][j] = (dp[i][j] + dp[i + 1][M - k]) % MOD

    return dp[0][M]
