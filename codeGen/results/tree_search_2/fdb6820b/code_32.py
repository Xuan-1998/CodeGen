def count_ways(A, N):
    MOD = 10**9 + 7
    dp = [0] * (N + 1)
    dp[0] = 1

    for i in range(1, N + 1):
        for j in range(m):
            if A[j] <= i:
                dp[i] += dp[i - A[j]]
                dp[i] %= MOD

    return dp[N]
