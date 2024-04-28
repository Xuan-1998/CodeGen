def maxSumOfSubsequence(nums, k):
    n = len(nums)
    dp = [[0] * (k + 1) for _ in range(n)]

    for i in range(n):
        dp[i][0] = nums[i]
        
        for j in range(1, min(i + 1, k) + 1):
            if i - j >= 0:
                dp[i][j] = max(dp[i][j], nums[i] + dp[i - j - 1][j - 1])
                
    return max(max(row) for row in dp)
