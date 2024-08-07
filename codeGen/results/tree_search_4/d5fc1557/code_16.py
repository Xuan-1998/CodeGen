def longest_subarray(nums):
    n = len(nums)
    dp = [0] * (n + 1)

    for i in range(1, n + 1):
        if nums[i - 1] == 1:
            dp[i] = max(dp[i - 1], dp[i - 1][j] + 1 for j in range(i) if nums[j] == 1)
        else:
            dp[i] = 0

    return max(dp)
