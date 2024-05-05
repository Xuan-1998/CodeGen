def solve():
    n = int(input())
    MOD = 998244353
    dp = [[0] * (n+2) for _ in range(n+2)]

    for i in range(1, n+2):
        dp[i][i] = 1

    for i in range(1, n+1):
        for j in range(1, min(i+1, n+2)):
            if i > 0:
                dp[i][j] = (dp[i-1][min(j-1, i)] + 1) % MOD
            else:
                dp[i][j] = 1

    return dp[n+1][n]%MOD

print(solve())
