def can_sum_divisible_by_m(nums, m):
    dp = [[0] * (m + 1) for _ in range(len(nums) + 1)]

    for i in range(1, len(nums) + 1):
        for j in range(m + 1):
            if nums[i - 1] <= j:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - nums[i - 1]] + nums[i - 1])
            else:
                dp[i][j] = dp[i - 1][j]

    return bool(dp[-1][-1] % m == 0)

# Example usage
n, m = map(int, input().split())
nums = list(map(int, input().split()))

print(can_sum_divisible_by_m(nums, m))
