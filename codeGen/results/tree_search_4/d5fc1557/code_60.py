from collections import defaultdict

def longestSubarray(nums):
    dp = defaultdict(int)
    max_length = 0
    for i, num in enumerate(nums):
        if num == 0:
            max_length = max(max_length, dp[i-1])
        else:
            dp[i] = dp.get(i-1, 0) + (dp.get(i-2, 0) if i > 0 and nums[i-1] == 1 else 0)
        max_length = max(max_length, dp[i])
    return max_length - 1
