def count_ways(m, n, arr):
    MOD = 10**9 + 7
    dp = [0] * (n + 1)
    dp[0] = 1

    for i in range(1, n + 1):
        for j in range(m):
            if i - arr[j] >= 0:
                dp[i] += dp[i - arr[j]]
                dp[i] %= MOD

    return dp[n]
