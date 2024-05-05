code
def max_score(arr, k, z):
    n = len(arr)
    dp = [[0] * (k + 1) for _ in range(n)]

    for i in range(1, n):
        for j in range(min(k, i - 1) + 1):
            if j <= z:
                dp[i][j] = max(dp[i-1][j], dp[i-1][z] + arr[i])
            else:
                dp[i][j] = max(dp[i-1][j], dp[i-1][k] + arr[i])

    return dp[n-1][k]
