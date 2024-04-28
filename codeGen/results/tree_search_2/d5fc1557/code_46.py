def longest_subarray(nums):
    n = len(nums)
    dp = [0] * (n + 1)

    max_length = 0
    for i in range(n):
        if nums[i] == 1:
            dp[i + 1] = dp[i] + 1
        else:
            dp[i + 1] = 0

        max_length = max(max_length, dp[i + 1])

    # Remove one element and find the longest subarray containing only 1's
    max_length_after_remove = 0
    for i in range(n):
        if nums[i] == 0:
            continue
        if max_length_after_remove < dp[i]:
            max_length_after_remove = dp[i]

    return max(max_length, max_length_after_remove)
