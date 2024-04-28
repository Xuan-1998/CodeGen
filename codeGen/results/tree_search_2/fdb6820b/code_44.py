def count_ways_to_form_N(A, N):
    MOD = 10**9 + 7
    dp = [0] * (N + 1)
    dp[0] = 1

    for i in range(1, N + 1):
        for num in A:
            if i >= num:
                dp[i] += dp[i - num]
                dp[i] %= MOD

    return dp[N]
