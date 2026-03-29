def solve(n):
    MOD = 998244353
    dp = [0] * (n + 2)
    dp[0] = 1

    for i in range(1, n + 2):
        for j in range(i):
            if (j & 1) == 0:
                continue
            dp[i] = max(dp[i], dp[j - 1] * binomial_coeff(i - 1, j - 1))
        dp[i] %= MOD

    return dp[n + 1]

def binomial_coeff(n, k):
    res = 1
    for i in range(k):
        res = (res * (n - i)) // (i + 1)
    return res
