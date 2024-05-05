def max_score(arr, k, z):
    n = len(arr)
    dp = [[float('-inf')] * (k + 1) for _ in range(n)]

    # Edge case: i = 1
    dp[0][0] = arr[0]

    for i in range(1, n):
        for j in range(min(i, k) + 1):
            if j == 0:
                dp[i][j] = max(dp[i-1][j], arr[i])
            else:
                dp[i][j] = max(dp[i-1][j], dp[i-1][min(j-1, z)] + arr[i])

    return dp[n-1][k]
