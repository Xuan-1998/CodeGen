def solve():
    n = int(input())
    mod = 998244353

    dp = [[0] * (n + 2) for _ in range(n + 1)]

    for i in range(n + 1):
        dp[i][0] = 1
    for j in range(1, n + 2):
        dp[0][j] = 0

    for i in range(1, n + 1):
        for j in range(1, n + 2):
            if j == 1:
                dp[i][j] = (dp[i-1][j-1] << 30) % mod
            else:
                dp[i][j] = (dp[i-1][j] << 30) % mod
                if i > 0 and j < n + 2:
                    dp[i][j] = (dp[i][j] + dp[i-1][j-1]) % mod

    return dp[n][n+1]
