N, M = map(int, input().split())
mod = 998244353

dp = [[[[0]*(M+1) for _ in range(M+1)] for _ in range(N+1)] for _ in range(N+1)]
dp[0][0][0][0] = 1

for i in range(N+1):
    for j in range(M+1):
        for k in range(j+1):
            for l in range(k+1):
                if dp[i][j][k][l] == 0:
                    continue
                if j < M:
                    dp[i][j+1][k][l] += dp[i][j][k][l]
                    dp[i][j+1][k][l] %= mod
                    dp[i][j+1][k+1][k+1] += dp[i][j][k][l]
                    dp[i][j+1][k+1][k+1] %= mod
                if i < N:
                    dp[i+1][j][0][0] += dp[i][j][k][l]
                    dp[i+1][j][0][0] %= mod

ans = 0
for i in range(M+1):
    ans += dp[N][M][i][i]
    ans %= mod

print(ans)

