def subset_sum_divisible(nums, m):
    n = len(nums)
    prefix_sums = [0] * (n + 1)
    for i in range(n):
        prefix_sums[i + 1] = (prefix_sums[i] + nums[i]) % m

    dp = [[False] * (m + 1) for _ in range(n + 1)]
    dp[0][0] = True

    for i in range(1, n + 1):
        for j in range(m + 1):
            if j >= nums[i - 1]:
                dp[i][j] = (dp[i - 1][j] or dp[i - 1][j - nums[i - 1]]) and prefix_sums[i] % m == j
            else:
                dp[i][j] = dp[i - 1][j]

    return any(dp[n][i] for i in range(m + 1))

n, m = map(int, input().split())
nums = list(map(int, input().split()))
print(subset_sum_divisible(nums, m))
