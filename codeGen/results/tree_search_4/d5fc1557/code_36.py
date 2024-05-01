def longestSubarray(nums):
    n = len(nums)
    dp = [0] * (n + 1)
    
    for i in range(1, n + 1):
        if nums[i-1] == 1:
            dp[i] = max(dp[i-1], 1) + 1
        else:
            dp[i] = 0
    
    return max(0, dp[-2])

import sys

n = int(input())
nums = [int(x) for x in input().split()]

print(longestSubarray(nums))
