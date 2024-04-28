def good_sequences(n, k):
    MOD = 1000000007

    dp = [[0] * (n + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        dp[i][1] = 1

    for j in range(2, n + 1):
        for i in range(j, n + 1):
            if j % i == 0:
                dp[i][j] = (dp[i][j - 1] + sum(dp[m][j // m] for m in range(1, j // i + 1))) % MOD

    return sum(dp[n][i] for i in range(k + 1)) % MOD
