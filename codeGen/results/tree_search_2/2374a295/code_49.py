def good_sequences(n, k):
    MOD = 1000000007

    dp = [[0] * (k + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, min(i + 1, k + 1)):
            if j == 1:
                dp[i][j] = 1
            elif j > 1 and (i % j) == 0:  # good sequence ending at i with remainder 0
                dp[i][j] = (dp[i - 1][j - 1] + dp[i // j][j]) % MOD

    return sum(dp[n][j] for j in range(1, k + 1)) % MOD

k, n = map(int, input().split())
print(good_sequences(n, k))
