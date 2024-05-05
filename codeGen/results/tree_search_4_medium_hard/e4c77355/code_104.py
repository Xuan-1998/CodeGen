def longest_increasing_subsequence(nums):
    n = len(nums)
    dp = [[1] * (n+1) for _ in range(n+1)]
    
    for i in range(1, n+1):
        for k in range(1, min(i+1, n+1)):
            if nums[i-1] > nums[i-k]:
                dp[i][k] = max(dp[i-1][0], k+1)
            else:
                dp[i][k] = 1
    
    return dp[n-1][0]
