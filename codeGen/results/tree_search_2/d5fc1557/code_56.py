def longestSubarray(nums):
    n = len(nums)
    dp = [0] * n
    max_length = 0
    
    for i in range(1, n):
        if nums[i] == 1:
            dp[i] = dp[i-1] + 1 if i > 0 else 1
        else:
            dp[i] = dp[i-1]
        max_length = max(max_length, dp[i])
    
    return max_length

import sys
n = int(input())
nums = list(map(int, input().split()))
print(longestSubarray(nums))
