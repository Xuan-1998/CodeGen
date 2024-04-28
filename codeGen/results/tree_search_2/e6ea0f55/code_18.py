def maxSumSubsequence(nums, k):
    n = len(nums)
    dp = [0] * n

    # Base cases: maximum sum at the first and last indices are the values of those elements themselves
    dp[0] = nums[0]
    dp[-1] = nums[-1]

    for i in range(1, n-1):
        if i - k >= 0:
            dp[i] = max(dp[i-1], nums[i] + dp[i-k])
        else:
            dp[i] = nums[i]

    return dp[-1]
