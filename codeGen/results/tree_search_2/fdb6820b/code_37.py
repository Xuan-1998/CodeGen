def count_ways(m, N, arr):
    dp = [0] * (N + 1)
    dp[0] = 1

    for i in range(1, N + 1):
        for k in range(m):
            if i - arr[k] >= 0:
                dp[i] += dp[i - arr[k]]

    return dp[N] % (10**9 + 7)
