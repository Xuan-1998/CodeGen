import sys

def longest_increasing_subsequence(nums):
    n = len(nums)
    m = max(nums) + 1
    dp = [[0] * m for _ in range(n)]

    for i in range(n):
        for j in range(m):
            if nums[i] > j:
                dp[i][j] = 1
            else:
                for k in range(i):
                    if nums[k] < nums[i] and dp[k][j-1]:
                        dp[i][j] = max(dp[i][j], dp[k][j-1] + 1)

    return max(max(row) for row in dp)

# Read input
nums = list(map(int, input().split()))

print(longest_increasing_subsequence(nums))
