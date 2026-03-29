import sys

def longest_increasing_subsequences(nums):
    n = len(nums)
    dp = [1] * n
    count = [0] * (n + 1)

    for i in range(1, n):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)

    for k in range(n + 1):
        count[k] = sum(x == k for x in dp)
    return count[-1]

nums = list(map(int, input().split()))
print(longest_increasing_subsequences(nums))
