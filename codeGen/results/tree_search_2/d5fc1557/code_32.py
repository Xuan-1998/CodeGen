def longest_subarray(nums):
    n = len(nums)
    dp = [0] * (n + 1)
    max_len = 0

    for i in range(n):
        if nums[i] == 1:
            dp[i+1] = max(dp[i], i+1)
        else:
            dp[i+1] = 1

        if i > 0 and nums[i] == 1:
            max_len = max(max_len, dp[i])

    return max_len - 1
