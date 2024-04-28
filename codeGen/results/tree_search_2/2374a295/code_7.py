def good_sequences(n, k):
    MOD = 1000000007

    dp = [[0] * (k + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for j in range(1, min(i, k) + 1):
            if j == 1:
                dp[i][j] = 1
            else:
                count = 0
                for x in range(1, i // j + 1):
                    if i % (x * j) == 0 and x <= n:
                        count += dp[x][j - 1]
                dp[i][j] = (count % MOD)

    return sum(dp[n][i] for i in range(k + 1)) % MOD
