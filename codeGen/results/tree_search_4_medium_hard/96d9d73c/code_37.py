def can_partition(A):
    N, K, M = map(int, input().split())
    A = list(map(int, input().split()))
    
    memo = {}
    dp = {}
    
    def dfs(i, j):
        if (i, j) in memo:
            return memo[(i, j)]
        
        if j == 0:
            return True
        
        if (i, j) not in dp:
            dp[(i, j)] = False
            for k in range(1, j + 1):
                sum_ = sum(A[i-k+1:i])
                if dfs(i - k, j-1) and all(abs(x - A[i-k]) <= M for x in A[i-k:i]):
                    dp[(i, j)] = True
                    break
        
        return dp[(i, j)]
    
    return dfs(N - 1, K)
