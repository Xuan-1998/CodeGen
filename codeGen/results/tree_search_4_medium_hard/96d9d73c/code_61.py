def canPartition(A, K, M):
    n = len(A)
    dp = [[0] * (K + 1) for _ in range(n + 1)]
    
    for i in range(K + 1):
        dp[0][i] = 1
    
    memo = {}
    
    def f(i, j):
        if (i, j) in memo:
            return memo[(i, j)]
        
        if dp[i][j]:
            return 1
        
        total = sum(A[:i])
        max_val = max(A[:i])
        
        if abs(total - max_val) > M or not f(i - 1, j):
            return 0
        
        for p in range(1, i + 1):
            if f(p - 1, j - 1) and all(abs(x - A[0]) <= M for x in A[:p]):
                return 1
        
        memo[(i, j)] = 0
        return 0
    
    return f(n, K)
