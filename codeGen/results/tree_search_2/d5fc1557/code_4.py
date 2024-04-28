def longestSubarray(nums):
    n = len(nums)
    dp = [0] * (n + 1)

    for i in range(1, n + 1):
        if nums[i - 1] == 1:
            if i == 1 or nums[i - 2] == 0:
                dp[i] = 1
            else:
                dp[i] = dp[i - 1] + 1
        else:
            dp[i] = max(dp[i - 1], 0)

    # Find the maximum length of a subarray containing only 1's
    max_length = 0
    for i in range(n, 0, -1):
        if nums[i - 1] == 1 and (i == n or nums[i - 2] == 0):
            max_length = dp[i]
            break

    return max_length
