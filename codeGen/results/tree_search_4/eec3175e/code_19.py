def checkSubarraySum(nums, k):
    n = len(nums)
    dp = [[False] * (k + 1) for _ in range(n + 1)]
    
    for i in range(n + 1):
        dp[i][0] = (i == 0 or sum(nums[:i]) % k == 0)
    
    for i in range(1, n + 1):
        for j in range(k + 1):
            if j == 0:
                dp[i][j] = True
            elif dp[i - 1][(j - nums[i]) % k]:
                dp[i][j] = True
    
    return any(dp[n][-1])
