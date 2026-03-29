def canPartition(A, K, M):
    N = len(A)
    dp = [[False for _ in range(K+1)] for _ in range(N+1)]
    
    # base cases
    dp[0][0] = True
    for i in range(1, N+1):
        dp[i][0] = False
    
    for i in range(1, N+1):
        for j in range(1, min(i//K+1, K)+1):
            if A[i-1]-A[i-K] <= M:
                dp[i][j] = True
            else:
                for k in range(1, i-K+1):
                    if dp[k][j-1]:
                        dp[i][j] = True
                        break
    
    return any(dp[N][k] for k in range(K, K+1))
