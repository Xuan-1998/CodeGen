import sys

def subset_sum_divisible(nums, m):
    n = len(nums)
    dp = [[False] * (m + 1) for _ in range(n + 1)]

    for i in range(n + 1):
        dp[i][0] = True

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if nums[i - 1] <= j:
                dp[i][j] = (dp[i-1][j] or dp[i-1][j-nums[i-1]])
            else:
                dp[i][j] = dp[i-1][j]

    return int(dp[n][m])

n, m = map(int, input().split())
nums = list(map(int, input().split()))
print(subset_sum_divisible(nums, m))
