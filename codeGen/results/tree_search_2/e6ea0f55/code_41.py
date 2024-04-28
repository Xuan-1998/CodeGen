from collections import defaultdict

def maxSumSubsequence(nums, k):
    n = len(nums)
    dp = [[0] * (k + 1) for _ in range(n)]
    
    # Initialize the first row of the DP table
    for j in range(k + 1):
        if j >= 1:
            dp[0][j] = nums[0]
        else:
            dp[0][j] = 0
    
    # Fill up the rest of the DP table
    for i in range(1, n):
        for j in range(min(i + 1, k) + 1):
            if j == 0:
                dp[i][j] = max(dp[i - 1][j], nums[i])
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - 1] + nums[i])
    
    # Find the maximum sum of a subsequence
    return max(sum(sub) for sub in (dp[i][:] for i in range(n)))

