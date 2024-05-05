def beautycontest(t, l, r):
    MOD = 10**9 + 7

    # Compute the minimum comparisons needed for each group size from l to r
    memo = [[-1] * (r + 1) for _ in range(t + 1)]
    
    def dfs(i, j):
        if i == t:
            return 0
        if memo[i][j] != -1:
            return memo[i][j]
        
        res = float('inf')
        for k in range(l, min(r, j) + 1):
            res = min(res, dfs(i + 1, k - 1) + (k - l + 1))
        
        memo[i][j] = res
        return res
    
    # Calculate the final answer
    res = sum((t - i) * dfs(i, j) for i in range(t) for j in range(l, r + 1)) % MOD
    
    return int(res)
