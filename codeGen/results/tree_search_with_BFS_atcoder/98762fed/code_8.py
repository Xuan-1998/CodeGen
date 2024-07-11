MOD = 998244353
N, M = map(int, input().split())
 
fact = [1]*(N*M+1)
inv = [1]*(N*M+1)
for i in range(1, N*M+1):
    fact[i] = fact[i-1]*i%MOD
    inv[i] = pow(fact[i], MOD-2, MOD)
 
def C(n, k):
    if n < k or k < 0:
        return 0
    return fact[n]*inv[k]*inv[n-k]%MOD
 
dp = [[[0]*(M+1) for _ in range(N+1)] for _ in range(max(N, M)+1)]
for i in range(1, max(N, M)+1):
    dp[i][1][i] = dp[i][i][1] = pow(2, i*(i-1)//2, MOD)
for i in range(2, N+1):
    for j in range(2, M+1):
        for k in range(1, max(i, j)+1):
            dp[k][i][j] = dp[k][i-1][j] + dp[k][i][j-1] - dp[k-1][i-1][j-1]
            for l in range(1, k):
                dp[k][i][j] += (C(i*l+j-k-1, i-1) + C(j*l+i-k-1, j-1) - C((i-1)*l+j-k-1, i-2) - C((j-1)*l+i-k-1, j-2))*pow(2, (i+j-l-2)*(l-1), MOD)*fact[l]%MOD
            dp[k][i][j] %= MOD
 
res = 0
for k in range(1, max(N, M)+1):
    res += dp[k][N][M]*pow(2, (N*M-k*(N+M-k)), MOD)
    res %= MOD
print(res)

