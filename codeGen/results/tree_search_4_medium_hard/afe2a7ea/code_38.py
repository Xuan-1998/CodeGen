def solve(n):
    MOD = 998244353

    dp = [0] * (n + 1)
    dp[0] = 1 if n > 0 else 0

    for i in range(1, n + 1):
        dp[i] = (dp[i - 1] * (i % MOD)) % MOD
        if i >= 2:
            dp[i] += (dp[i - 1] * ((n - i) % MOD)) % MOD

    return dp[n]
