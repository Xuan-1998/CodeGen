dp = {}
def max_sum(arr, k):
    n = len(arr)
    for i in range(n+1):
        dp[i] = {}
        for j in range(1, min(i, k)+1):
            if j == 1:
                dp[i][j] = max(arr[:i])
            else:
                dp[i][j] = max(dp[prev][j-1], arr[prev:i]) + max_sum(arr[prev:i], j-1)
    return dp[n][k]
