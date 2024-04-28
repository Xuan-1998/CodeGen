def count_good_sequences(n, k):
    MOD = 1000000007

    dp = [0] * (n + 1)
    dp[1] = 1  # base case: only one good sequence ending with 1

    for i in range(2, n + 1):
        dp[i] = sum(dp[j] for j in range(1, i))
        dp[i] %= MOD

    return dp[n] % MOD
