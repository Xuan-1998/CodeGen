def can_partition_subset_sum(arr, m):
    max_value = max(arr)
    dp = [[False] * (n + 1) for _ in range((m * max_value) + 1)]

    for i in range(n + 1):
        dp[0][i] = True

    for sum in range(1, (m * max_value) + 1):
        for i in range(1, n + 1):
            if arr[i - 1] <= sum:
                dp[sum][i] = dp[sum % m][i - 1] or dp[sum - arr[i - 1]][i - 1]
            else:
                dp[sum][i] = dp[sum][i - 1]

    return int(dp[m * max_value][n])
