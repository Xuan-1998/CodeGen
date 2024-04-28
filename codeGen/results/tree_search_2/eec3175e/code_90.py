def subsetSumDivisible(arr, m):
    n = len(arr)
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(n + 1):
        dp[i][0] = 1

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if arr[i - 1] % m == 0:
                dp[i][j] = dp[i - 1][j]
            elif dp[i - 1][j] == 1 or (j - arr[i - 1]) % m in range(m + 1):
                dp[i][j] = 1
            else:
                dp[i][j] = 0

    return int(dp[n][m])
