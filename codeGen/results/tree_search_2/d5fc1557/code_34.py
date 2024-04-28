def longest_subarray(nums):
    n = len(nums)
    max_len = 0
    dp = [0] * (n + 1)  # Initialize dp array with zeros

    for i in range(1, n + 1):
        if nums[i - 1] == 1:
            dp[i] = dp[i - 1] + 1  # Update dp[i] only when the current element is 1
            max_len = max(max_len, dp[i])  # Update max_len if we find a longer subarray

    return max_len
