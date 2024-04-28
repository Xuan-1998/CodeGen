def longest_subarray(nums):
    n = len(nums)
    dp = [0] * (n + 1)  # Initialize dp with zeros
    max_length = 0

    for i in range(1, n + 1):
        if nums[i - 1] == 1:
            dp[i] = dp[i - 1] + 1
        else:
            dp[i] = 0
        max_length = max(max_length, dp[i])

    return max_length - 1
