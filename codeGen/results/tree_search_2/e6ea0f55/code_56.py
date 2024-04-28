def maxSumSubsequence(nums, k):
    n = len(nums)
    dp = [0] * (n + 1)  # Initialize the state array

    for i in range(1, n + 1):
        for j in range(max(0, i - k), i):  # Iterate from i-k to i
            dp[i] = max(dp[i], dp[j - 1] + nums[i - 1]) if j > 0 else nums[i - 1]

    return dp[-1]
