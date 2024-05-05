def max_xor_sum(A, X):
    N = len(A)
    dp = [[0] * (N + 1) for _ in range(N + 1)]
    
    for i in range(1, N + 1):
        for j in range(1, min(i + 1, N)):
            dp[i][j] = max(dp[j - 1][j - 1] + (A[j - 1] - X) ^ A[j], 
                           dp[j - 1][j] + (A[j] - X) ^ A[j])
    
    return dp[N][N]
