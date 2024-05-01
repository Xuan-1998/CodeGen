def longestSubarray(nums):
    n = len(nums)
    dp = {0: 0}
    ans = 0
    
    for i, x in enumerate(nums):
        if x == 1:
            dp[i+1] = dp.get(i, 0) + 1
            ans = max(ans, dp[i+1])
        else:
            dp.pop(i)
    
    return n - (max(dp.keys()) if dp else -1)

# Example usage:
import sys

n = int(input().strip())
nums = [int(x) for x in input().strip().split()]

print(longestSubarray(nums))
