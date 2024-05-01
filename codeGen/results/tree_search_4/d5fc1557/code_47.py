def longest_subarray(nums):
    n = len(nums)
    dp = {0: 0}
    max_length = 0

    for i in range(n):
        if nums[i] == 1:
            dp[i+1] = dp.get(i, 0) + 1
            max_length = max(max_length, dp[i+1])
        else:
            dp.pop(i, None)

    return max_length
