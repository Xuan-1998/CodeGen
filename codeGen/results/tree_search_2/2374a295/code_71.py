def good_sequences(n, k):
    MOD = 1000000007

    dp = [0] * (n + 1)
    for i in range(2, n + 1):
        if all(i % j == 0 for j in range(2, int(i ** 0.5) + 1)):
            dp[i] = sum(dp[j // k] for k in range(2, i)) % MOD
        else:
            dp[i] = 0

    return dp[n] % MOD


n, k = map(int, input().split())
print(good_sequences(n, k))
