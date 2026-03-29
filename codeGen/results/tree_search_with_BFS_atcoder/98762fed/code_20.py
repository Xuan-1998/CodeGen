MOD = 998244353
N, M = map(int, input().split())
dp = [[[[0]*401 for _ in range(401)] for _ in range(401)] for _ in range(401)]
for i in range(N+1):
    for j in range(M+1):
        dp[i][j][i][j] = 1
for len1 in range(N+1):
    for len2 in range(M+1):
        for i in range(N-len1+1):
            for j in range(M-len2+1):
                k, l = i + len1 - 1, j + len2 - 1
                dp[i][j][k][l] += dp[i+1][j][k][l] + dp[i][j+1][k][l] - dp[i+1][j+1][k][l]
                dp[i][j][k][l] %= MOD
                if k < N:
                    dp[i][j][k+1][l] += dp[i][j][k][l]
                    dp[i][j][k+1][l] %= MOD
                if l < M:
                    dp[i][j][k][l+1] += dp[i][j][k][l]
                    dp[i][j][k][l+1] %= MOD
print(dp[0][0][N][M])

