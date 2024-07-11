MOD = 998244353
N, M = map(int, input().split())
dp = [[0]*(M+1) for _ in range(N+1)]
pow2 = [1]
for _ in range(N*M):
    pow2.append(pow2[-1]*2%MOD)

for i in range(1, N+1):
    for j in range(1, M+1):
        if i == 1 and j == 1:
            dp[i][j] = 2
        else:
            dp[i][j] = (dp[i-1][j]*pow2[j] + dp[i][j-1]*pow2[i]) % MOD

print(dp[N][M])

