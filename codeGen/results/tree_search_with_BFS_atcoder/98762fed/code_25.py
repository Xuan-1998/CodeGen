MOD = 998244353
N, M = map(int, input().split())
pow2 = [1]*(N*M+1)
for i in range(1, N*M+1):
    pow2[i] = pow2[i-1]*2%MOD

fact = [1]*(N*M+1)
inv = [1]*(N*M+1)
for i in range(1, N*M+1):
    fact[i] = fact[i-1]*i%MOD
    inv[i] = pow(fact[i], MOD-2, MOD)

def comb(n, k):
    if n < k or n < 0 or k < 0:
        return 0
    return fact[n]*inv[k]*inv[n-k]%MOD

dp = [[0]*(M+1) for _ in range(N+1)]
for i in range(1, N+1):
    for j in range(1, M+1):
        dp[i][j] = pow2[i*j]
        for k in range(1, i):
            dp[i][j] -= comb(i, k)*dp[k][j]%MOD
        for k in range(1, j):
            dp[i][j] -= comb(j, k)*dp[i][k]%MOD
        dp[i][j] %= MOD
print(dp[N][M])

