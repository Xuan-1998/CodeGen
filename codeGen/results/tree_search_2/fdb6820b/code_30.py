def countWays(n, nums):
    dp = [[0] * (len(nums) + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for j in range(1, len(nums) + 1):
            if nums[j - 1] <= i:
                dp[i][j] = sum(dp[i - x][k] for k in range(j)) % (10**9 + 7)
    
    return dp[n][len(nums)]
