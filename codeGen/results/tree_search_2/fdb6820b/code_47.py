def count_ways(m, N, A):
    MOD = 10**9 + 7
    dp = [0] * (N + 1)
    for i in range(m):
        for j in range(N + 1):
            if j >= A[i]:
                dp[j] += dp[j - A[i]]
            dp[j] %= MOD

    return dp[N]
