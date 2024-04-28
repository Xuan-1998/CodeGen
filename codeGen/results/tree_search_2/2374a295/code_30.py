def count_good_sequences(n, k):
    MOD = 1000000007

    dp = {0: 1}

    for i in range(1, n+1):
        dp[i] = 0
        for j in range(i, n//i+1):
            if j != i:
                continue
            dp[i] += dp[j-1]
            dp[i] %= MOD

    return sum(dp.values()) % MOD

n, k = map(int, input().split())
print(count_good_sequences(n, k))
