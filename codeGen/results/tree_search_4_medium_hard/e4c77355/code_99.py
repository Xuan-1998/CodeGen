=code block starts=
from collections import defaultdict

def lengthOfLIS(nums):
    dp = [1] * len(nums)
    memo = {}

    for i in range(len(nums)):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)
                memo[(j, i)] = dp[i]
        dp[i] = max(1, dp[i])

    return max(dp)

=code block ends=
