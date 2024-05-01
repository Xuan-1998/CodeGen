def can_sum_divisible_by_m(arr, m):
    n = len(arr)
    dp = [[False for _ in range(m)] for _ in range(n + 1)]

    dp[0][0] = True

    for i in range(1, n + 1):
        for j in range(m):
            if j < arr[i - 1]:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = dp[i - 1][j] or (dp[i - 1][(j - arr[i - 1]) % m] and (j + arr[i - 1]) % m == 0)

    return any(dp[n - 1][i] for i in range(m))
