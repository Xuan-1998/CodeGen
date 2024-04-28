def longest_subarray(nums):
    n = len(nums)
    dp = {0: 0}
    max_length = 0

    for i in range(1, n):
        if nums[i] == 1 and (i - 1 not in dp or dp[i-1] < dp.get(i-1, 0)):
            dp[i] = dp.get(i-1, 0) + 1
            max_length = max(max_length, dp[i])
        else:
            dp[i] = 0

    return max_length
