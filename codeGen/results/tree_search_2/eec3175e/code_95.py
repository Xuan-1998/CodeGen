def can_sum_divisible(nums, m):
    n = len(nums)
    dp = [[False] * (m+1) for _ in range(n+1)]

    # Base case: empty subset has sum 0
    dp[0][0] = True

    for i in range(1, n+1):
        for j in range(m+1):
            if nums[i-1] <= j:
                dp[i][j] = (dp[i-1][j%nums[i-1]] or (j - nums[i-1]) % m == 0)
            else:
                dp[i][j] = dp[i-1][j]

    return int(any(dp[n][i] for i in range(m+1)))

# Example usage:
nums = [3, 5, 7]
m = 10
print(can_sum_divisible(nums, m))  # Output: 1 (because the subset {3, 7} has sum divisible by 10)
