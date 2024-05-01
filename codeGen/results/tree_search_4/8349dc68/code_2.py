def maxSumAfterPartitioning(arr, k):
    n = len(arr)
    dp = [0] * (n + 1)
    
    memo = {}
    
    def dfs(i):
        if i > k:
            return dp[i-k]
        elif i in memo:
            return memo[i]
        
        res = max(arr[i], arr[i-1]+arr[i-2]+...+arr[max(0, i-k)])
        dp[i] = res
        memo[i] = res
        
        if i > k:
            dp[i-k] = max(dp[i-k], dp[i])
        
        return dp[i]
    
    return dfs(n)
