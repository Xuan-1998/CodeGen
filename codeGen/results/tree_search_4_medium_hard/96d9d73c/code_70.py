def canBePartitioned(N, K, M, A):
    dp = [[False for _ in range(K+1)] for _ in range(N)]
    
    # Initialize base case
    for i in range(N):
        dp[i][0] = True
    
    for i in range(1, N):
        for j in range(min(i // K + 1, M) + 1):
            if j == 0:
                continue
            
            max_val = max(A[:i])
            min_val = min(A[i:])
            
            diff = abs(max_val - min_val)
            
            # If the difference is less than or equal to M and we have enough partitions
            if diff <= M and i >= K:
                for p in range(i):
                    if dp[p][j-1] and all(abs(x-A[0]) <= M for x in A[p+K:i]):
                        dp[i][j] = True
                        break
    
    return dp[-1][-1]
