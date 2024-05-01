def distinct_sum_set(nums):
    n, total = len(nums), sum(nums)
    dp = [[False] * (total + 1) for _ in range(n + 1)]
    
    memo = {}
    
    def dfs(i, j):
        if (i, j) in memo:
            return memo[(i, j)]
        
        if i > n or j < 0:
            return False
        
        dp[i][j] = (dp[i-1][j] if i > 0 else True) or (nums[i-1] <= j and dfs(i-1, j-nums[i-1]))
        
        memo[(i, j)] = dp[i][j]
        return dp[i][j]
    
    result = []
    for j in range(total + 1):
        if dfs(n, j):
            result.append(j)
    
    return ' '.join(map(str, result))
