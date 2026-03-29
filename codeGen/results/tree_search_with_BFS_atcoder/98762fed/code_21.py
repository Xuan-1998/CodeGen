def solve(N, M):
    mod = 998244353
    dp = [[[[0]*(M+1) for _ in range(N+1)] for _ in range(M+1)] for _ in range(N+1)]
    dp[0][0][0][0] = 1
    for i in range(N+1):
        for j in range(M+1):
            for k in range(i+1):
                for l in range(min(j,k)+1):
                    if i < N:
                        dp[i+1][j][k][l] = (dp[i+1][j][k][l] + dp[i][j][k][l] * (k+1)) % mod
                        dp[i+1][j][k+1][l] = (dp[i+1][j][k+1][l] + dp[i][j][k][l] * (i+1-k)) % mod
                    if j < M:
                        dp[i][j+1][k][l] = (dp[i][j+1][k][l] + dp[i][j][k][l] * (l+1)) % mod
                        dp[i][j+1][k][l+1] = (dp[i][j+1][k][l+1] + dp[i][j][k][l] * (j+1-l)) % mod
    return dp[N][M][N][M]

N, M = map(int, input().split())
print(solve(N, M))

