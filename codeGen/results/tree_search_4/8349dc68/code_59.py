def max_sum_after_partitioning(arr, k):
    n = len(arr)
    dp = [[0] * (k + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(min(i, k) + 1):
            if j == 0:
                dp[i][j] = max(dp[i - 1])
            else:
                max_val = max(arr[i - j:i])
                if max_val > dp[i - j][j - 1]:
                    dp[i][j] = max_val + sum(arr[:i - j])
                else:
                    dp[i][j] = dp[i - j][j - 1]

    return dp[n][k]
