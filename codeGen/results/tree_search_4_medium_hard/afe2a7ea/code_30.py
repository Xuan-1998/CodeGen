def find_probability(n):
    mod = 998244353
    dp = [[0] * (n + 2) for _ in range(n + 2)]
    for i in range(n + 1):
        dp[0][i] = 1
    for i in range(1, n + 2):
        for j in range(i - 1, n + 1):
            if i == n + 1:
                break
            for k in range(j - 1, i - 1, -1):
                dp[i][j] = (dp[i][j] + dp[k][j - 1]) % mod
    return dp[n + 1][n]
