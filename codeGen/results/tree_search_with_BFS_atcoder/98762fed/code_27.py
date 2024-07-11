MOD = 998244353
N, M = map(int, input().split())
dp = [[[[0]*(M+1) for _ in range(N+1)] for _ in range(M+1)] for _ in range(N+1)]
dp[0][0][0][0] = 1
for i in range(N+1):
    for j in range(M+1):
        for k in range(i+1):
            for l in range(j+1):
                if i < N:
                    dp[i+1][j][k][l] += dp[i][j][k][l]
                    dp[i+1][j][i+1][l] += dp[i][j][k][l]
                    dp[i+1][j][k][l] %= MOD
                    dp[i+1][j][i+1][l] %= MOD
                if j < M:
                    dp[i][j+1][k][l] += dp[i][j][k][l]
                    dp[i][j+1][k][j+1] += dp[i][j][k][l]
                    dp[i][j+1][k][l] %= MOD
                    dp[i][j+1][k][j+1] %= MOD
res = 0
for i in range(N+1):
    for j in range(M+1):
        res += dp[N][M][i][j]
        res %= MOD
print(res)

