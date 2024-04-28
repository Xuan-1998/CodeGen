def max_sum_of_subsequence(nums, k):
    n = len(nums)
    dp = [0] * n  # Initialize the dynamic programming table

    # Base cases: the maximum sum for the first and last elements is their value itself
    dp[0] = nums[0]
    dp[-1] = nums[-1]

    # Fill up the table using dynamic programming
    for i in range(1, n - 1):
        max_sum = 0
        for j in range(max(0, i - k), min(n, i + k + 1)):
            max_sum = max(max_sum, dp[j] + nums[i])
        dp[i] = max_sum

    # Return the maximum sum of a subsequence ending at any index
    return max(dp)
