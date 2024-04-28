def longest_subarray(nums):
    n = len(nums)
    dp = {0: 0}
    max_length = 0

    for i in range(1, n):
        if nums[i] == 1:
            dp[i] = dp.get(i-1, 0) + 1
            max_length = max(max_length, dp[i])
        else:
            dp.pop(i-1)
            max_length = 0

    return max_length
