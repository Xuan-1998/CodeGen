import sys
from collections import defaultdict

def canJump(nums):
    dp = defaultdict(bool)
    dp[0] = True
    for i in range(len(nums)):
        if not dp[i]:
            continue
        for j in range(i+1, min(i+nums[i]+1, len(nums))):
            dp[j] = True
    return dp[-1]

# Example usage:
n = int(input())
nums = list(map(int, input().split()))
print(canJump(nums))
