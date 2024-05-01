def longest_subarray(nums):
    n = len(nums)
    dp = [-1] * (n + 1)
    
    for i in range(n):
        if nums[i] == 0:
            dp[i + 1] = max(dp[i + 1], dp[i])
        elif i > 0 and nums[i] == 1:
            dp[i + 1] = max(dp[i], dp[i - 1] + 1)
    
    return max(0, dp[-2])
