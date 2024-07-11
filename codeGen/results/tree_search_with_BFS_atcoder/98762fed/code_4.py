from math import comb

MOD = 998244353
N, M = map(int, input().split())

dp = [[[0 for _ in range(M+1)] for _ in range(M+1)] for _ in range(N+1)]
dp[0][0][0] = 1

for i in range(N+1):
    for j in range(M+1):
        for k in range(j+1):
            if i+j == 0:
                continue
            dp[i][j][k] = dp[i-1][j][k] if i > 0 else 0
            if k > 0:
                dp[i][j][k] += dp[i][j][k-1]
            if j > 0:
                dp[i][j][k] += dp[i][j-1][k] * 2 if k > 0 else 0
                dp[i][j][k] += dp[i][j-1][j-1] - dp[i][j-1][k-1] if k > 0 else 0
            dp[i][j][k] %= MOD

print(sum(dp[N][M][k] for k in range(M+1)) % MOD)

