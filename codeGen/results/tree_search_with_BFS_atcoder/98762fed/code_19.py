MOD = 998244353
N, M = map(int, input().split())

# pre-calculate binomial coefficients
C = [[0]*(M+1) for _ in range(M+1)]
C[0][0] = 1
for i in range(1, M+1):
    C[i][0] = 1
    for j in range(1, i+1):
        C[i][j] = (C[i-1][j-1] + C[i-1][j]) % MOD

# dynamic programming
dp = [[[0]*(M+1) for _ in range(N+1)] for _ in range(M+1)]
dp[0][0][0] = 1
for i in range(M+1):
    for j in range(N+1):
        for k in range(M+1):
            if dp[i][j][k] == 0:
                continue
            for l in range(M-k+1):
                dp[i+l][j+1][k+l] += dp[i][j][k] * C[M-i][l] * pow(2, M-l, MOD)
                dp[i+l][j+1][k+l] %= MOD

# calculate the answer
ans = 0
for i in range(M+1):
    ans += dp[i][N][M] * pow(2, i*(N-1), MOD)
    ans %= MOD

print(ans)

