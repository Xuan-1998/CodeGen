def count_ways_to_form_n(A, N):
    MOD = 10**9 + 7

    # Initialize the DP table
    dp = [0] * (N + 1)
    dp[0] = 1

    for i in range(len(A)):
        for j in range(N, A[i] - 1, -1):
            dp[j] += dp[j - A[i]]
            dp[j] %= MOD

    return dp[N]
