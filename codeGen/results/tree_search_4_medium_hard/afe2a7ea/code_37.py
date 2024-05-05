def probability(n):
    MOD = 998244353
    dp = [0] * (n + 2)
    dp[0] = 1

    for i in range(1, n + 2):
        for j in range(i):
            if j % 2 == 0:
                dp[i] += dp[j]
                dp[i] %= MOD
            else:
                dp[i] -= dp[j]
                dp[i] %= MOD

    return dp[n + 1]

n = int(input())
print(probability(n))
