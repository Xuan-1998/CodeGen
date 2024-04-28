import sys

def longestSubarray(nums):
    n = len(nums)
    dp = [0] * (n + 1)

    for i in range(n):
        if nums[i] == 1:
            dp[i+1] = max(dp[i], dp[i-1]+1) if i > 0 else 1
        else:
            dp[i+1] = dp[i]

    return max(0, max(dp[:-1]) - 1)

n = int(input())
nums = [int(x) for x in input().split()]
print(longestSubarray(nums))
