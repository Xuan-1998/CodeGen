def findNumberOfLIS(nums):
    n = len(nums)
    dp = {i: 1 for i in range(n)}
    max_length = 1

    for i in range(1, n):
        for j in range(i):
            if nums[i] > nums[j]:
                if dp[i] < dp[j] + 1:
                    dp[i] = dp[j] + 1
                if dp[i] == dp[j] + 1:
                    max_length += 1

    return max_length
