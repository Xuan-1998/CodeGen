def good_sequences(n, k):
    MOD = 10000000007

    dp = {0: 1}

    for i in range(1, n+1):
        if i <= k:
            dp[i] = sum((j+1)*dp.get((k-1) // (i/j), 0) for j in range(i))
        else:
            break

    return dp[k] % MOD
