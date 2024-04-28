def good_sequences(n, k):
    dp = [[0] * (n + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(i, n + 1):
            if i % j != 0:
                continue
            dp[i][j] = sum(dp[k][j] for k in range(1, i // j))
            dp[i][j] %= 100000007

    return dp[n][k]
