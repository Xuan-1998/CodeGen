def can_sum_subset_divisible(nums, m):
    n = len(nums)
    dp = [[False] * (m + 1) for _ in range(n + 1)]

    dp[0][0] = True

    for i in range(1, n + 1):
        for j in range(m + 1):
            if nums[i - 1] % m == 0:
                dp[i][j] = (dp[i - 1][j // m] or not j % m) and any(dp[k][j - k * m] for k in range(i))
            else:
                dp[i][j] = (not j % m and any(dp[k][j - k * m] for k in range(i))) or dp[i - 1][j]

    return int(any(dp[n][i] for i in range(m + 1)))

# Example usage
n, m = map(int, input().split())
nums = list(map(int, input().split()))
print(can_sum_subset_divisible(nums, m))
