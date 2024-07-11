MOD = 998244353
N, M = map(int, input().split())

# Precompute factorials and inverse factorials
fact = [1]*(N*M+1)
inv_fact = [1]*(N*M+1)
for i in range(1, N*M+1):
    fact[i] = fact[i-1]*i % MOD
    inv_fact[i] = pow(fact[i], MOD-2, MOD)

# Binomial coefficient
def choose(n, k):
    return fact[n]*inv_fact[k]*inv_fact[n-k] % MOD

# DP table
dp = [[[[0]*(M+1) for _ in range(N+1)] for _ in range(M+1)] for _ in range(N+1)]
dp[0][0][0][0] = 1

for i in range(N+1):
    for j in range(M+1):
        for k in range(i+1):
            for l in range(j+1):
                if i < N:
                    # Add a new row
                    for x in range(l+1):
                        dp[i+1][j][x][l] += dp[i][j][k][l]*choose(M, x)*choose(M-k, x-l) % MOD
                        dp[i+1][j][x][l] %= MOD
                if j < M:
                    # Add a new column
                    for y in range(k+1):
                        dp[i][j+1][k][y] += dp[i][j][k][l]*choose(N, y)*choose(N-l, y-k) % MOD
                        dp[i][j+1][k][y] %= MOD

# Sum up all valid matrices
ans = 0
for k in range(N+1):
    for l in range(M+1):
        ans += dp[N][M][k][l]
        ans %= MOD
print(ans)

