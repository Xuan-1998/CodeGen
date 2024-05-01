def longest_subarray(nums):
    n = len(nums)
    dp = [0] * n
    prev_ones = 0

    for i in range(n):
        if nums[i] == 1:
            prev_ones += 1
        else:
            dp[i] = max(prev_ones, 0)
            prev_ones = 0

    return max(dp)
