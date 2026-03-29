def canPartition(K, M, A):
    N = len(A)
    dp = [[False for _ in range(K+1)] for _ in range(N+1)]
    
    for i in range(N+1):
        if i == 0:
            dp[i][0] = True
        else:
            for j in range(1, min(i//K+1, K)+1):
                dp[i][j] = False
                
                # If the current element is less than or equal to K
                if A[i-1] <= K:
                    for k in range(j-1, 0, -1):
                        if (dp[i-1][k-1] and abs(A[i-1]-A[i-k]) <= M):
                            dp[i][j] = True
                            break
                
                # If the current element is greater than K
                else:
                    for k in range(j-1, 0, -1):
                        if (dp[i-1][k-1] and A[i-1]-A[i-k-1] > M):
                            dp[i][j] = True
                            break

    return any(dp[N][i] for i in range(1, K+1))
