import sys

def longest_subarray(nums):
    n = len(nums)
    dp = [0] * (n + 1)
    for i in range(1, n + 1):
        if nums[i - 1] == 1:
            dp[i] = max(dp[i], dp[i - 1])
        else:
            dp[i] = 0
    result = max(dp[1:])
    return result

n = int(input())
nums = list(map(int, input().split()))
print(longest_subarray(nums))
