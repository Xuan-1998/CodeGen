N, M = map(int, input().split())
mod = 998244353

dp = [[[[0, 0] for _ in range(M+1)] for _ in range(N+1)] for _ in range(N+1)]
dp[0][0][0][0] = 1

for i in range(N+1):
    for j in range(M+1):
        for k in range(j+1):
            for l in range(2):
                if i < N:
                    dp[i+1][j][k][0] = (dp[i+1][j][k][0] + dp[i][j][k][l]) % mod
                    if k < j:
                        dp[i+1][j][k+1][1] = (dp[i+1][j][k+1][1] + dp[i][j][k][l]) % mod
                if j < M:
                    dp[i][j+1][k][0] = (dp[i][j+1][k][0] + dp[i][j][k][l]) % mod
                    if l == 1:
                        dp[i][j+1][k+1][1] = (dp[i][j+1][k+1][1] + dp[i][j][k][l]) % mod

result = 0
for i in range(N+1):
    for j in range(i+1):
        for k in range(2):
            result = (result + dp[i][M][j][k]) % mod

print(result)

