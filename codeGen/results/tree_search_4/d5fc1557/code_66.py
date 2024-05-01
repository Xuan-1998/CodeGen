from collections import defaultdict

def longestSubarray(nums):
    n = len(nums)
    dp = [0] * (n + 1)

    memo = defaultdict(int)

    for i in range(1, n + 1):
        if nums[i - 1] == 1:
            dp[i] = dp[i - 1] + 1
        else:
            if i > 1 and nums[i - 2] == 1:
                dp[i] = dp[i - 2]
            else:
                dp[i] = 0

    return max(dp)

