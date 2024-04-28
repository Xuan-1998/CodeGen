def dp(n, k):
    MOD = 1000000007
    dp = [0] * (n + 1)
    dp[0] = 1
    for i in range(1, n):
        dp[i] = sum(dp[:i])
        if i % j == 0:
            dp[i] += dp[j - 1]
    return dp[k]

n, k = map(int, input().split())
print(dp(n, k) % MOD)
