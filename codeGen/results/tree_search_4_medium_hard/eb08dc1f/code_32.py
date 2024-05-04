def solve(n):
    MOD = 998244353

    dp = [[0]*(n+1) for _ in range(11)]
    dp[0][0] = 1

    for k in range(1, n+1):
        for j in range(k, 0, -1):
            for i in range(j-1, -1, -1):
                if (k-j+1) >= i:
                    dp[k][j] += dp[i][min(i, j)]
                    dp[k][j] %= MOD

    return ' '.join(str(dp[n][i]) for i in range(1, n+1))

n = int(input())
print(solve(n))
