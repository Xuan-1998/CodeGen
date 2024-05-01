def longest_subarray(nums):
    n = len(nums)
    dp = [0] * (n + 1)
    ones = 0
    
    for i in range(n):
        if nums[i] == 1:
            ones += 1
        else:
            ones = 0
        
        dp[i + 1] = max(dp[i], ones)
    
    return max(dp)
