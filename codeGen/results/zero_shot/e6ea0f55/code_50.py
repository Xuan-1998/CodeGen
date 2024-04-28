def max_sum_subsequence(nums, k):
    n = len(nums)
    dp = [0] * (n + 1)
    
    for i in range(1, n + 1):
        dp[i] = max(dp[i - 1], nums[i - 1])
        
    res = dp[0]
    for i in range(k + 1):
        if i > 0:
            for j in range(i, n):
                res = max(res, dp[j] + (nums[j] - nums[j - i]) if j >= i else nums[j])
        dp[0] += 1
    print(res)
