def longestSubarray(nums):
    n = len(nums)
    max_len = 0

    dp = [0] * (n + 1)
    for i in range(n):
        if nums[i] == 1:
            dp[i + 1] = dp[i] + 1
            max_len = max(max_len, dp[i + 1])

    # Find the maximum length of consecutive ones
    max_ones = max(dp)

    # If there is no subarray containing only 1's, return 0
    if max_ones == 0:
        return 0

    # Calculate the length of the longest subarray containing only 1's
    longest_subarray_len = n - (max_ones + 1)
    
    return longest_subarray_len
