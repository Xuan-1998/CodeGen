MOD = 998244353
N, M = map(int, input().split())
fact = [1 for _ in range(N*M+1)]
inv = [1 for _ in range(N*M+1)]
fact_inv = [1 for _ in range(N*M+1)]
for i in range(1, N*M+1):
    fact[i] = fact[i-1] * i % MOD
    inv[i] = pow(i, MOD-2, MOD)
    fact_inv[i] = fact_inv[i-1] * inv[i] % MOD
dp = [[[[0 for _ in range(M+1)] for _ in range(N+1)] for _ in range(M+1)] for _ in range(N+1)]
for i in range(N+1):
    for j in range(M+1):
        dp[i][j][i][j] = 1
for d_i in range(N+1):
    for d_j in range(M+1):
        for i in range(N-d_i+1):
            for j in range(M-d_j+1):
                k = i + d_i
                l = j + d_j
                dp[i][j][k][l] += dp[i+1][j][k][l] * fact[k-i+l-j-1] * fact_inv[k-i-1] % MOD * fact_inv[l-j] % MOD
                dp[i][j][k][l] += dp[i][j+1][k][l] * fact[k-i+l-j-1] * fact_inv[k-i] % MOD * fact_inv[l-j-1] % MOD
                dp[i][j][k][l] -= dp[i+1][j+1][k][l] * fact[k-i+l-j-2] * fact_inv[k-i-1] % MOD * fact_inv[l-j-1] % MOD
                dp[i][j][k][l] %= MOD
print(dp[0][0][N][M])

