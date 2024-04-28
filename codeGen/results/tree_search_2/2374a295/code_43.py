def good_sequences(n, k):
    MOD = 1000000007

    dp = [0] * (n + 1)
    for i in range(1, n + 1):
        count = sum(j % i == 0 for j in range(1, n + 1))
        dp[i] = count
        if i >= k:
            good_count = sum(j % i == 0 for j in range(1, i))
            dp[i] += good_count

    return dp[n] % MOD


n, k = map(int, input().split())
print(good_sequences(n, k))
