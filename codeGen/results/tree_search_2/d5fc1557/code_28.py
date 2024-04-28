import sys

def longest_ones(nums):
    n = len(nums)
    dp = {i: 0 for i in range(n)}
    max_length = 0

    for i in range(1, n):
        if nums[i] == 1:
            dp[i] = dp.get(i-1, 0) + 1
            max_length = max(max_length, dp[i])
        else:
            dp[i] = 0

    return max_length - 1 if max_length > 0 else 0


# Read input from stdin
n = int(input())
nums = list(map(int, input().split()))

print(longest_ones(nums))
