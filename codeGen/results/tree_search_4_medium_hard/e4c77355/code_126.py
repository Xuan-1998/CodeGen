def longest_increasing_subsequence(nums):
    n = len(nums)
    dp = [1] * n  # initialize dp table with ones

    for i in range(1, n):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)

    return max(dp)  # return the maximum value in dp
