def can_subset_divide(m, nums):
    n = len(nums)
    dp = [[False] * m for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(m):
            if j < nums[i - 1]:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = dp[i - 1][j % (nums[i - 1] + 1)] or dp[i - 1][j]

    return any(dp[n][i] for i in range(m))

# Read inputs from stdin
n, m = map(int, input().split())
nums = list(map(int, input().split()))

print(can_subset_divide(m, nums))
