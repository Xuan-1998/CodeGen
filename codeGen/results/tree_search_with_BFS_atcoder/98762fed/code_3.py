MOD = 998244353
N, M = map(int, input().split())

# Pre-calculate powers of 2
pow2 = [1]*(N*M+1)
for i in range(1, N*M+1):
    pow2[i] = pow2[i-1]*2%MOD

# Initialize DP table
dp = [[0]*(M+1) for _ in range(N+1)]
for i in range(N+1):
    dp[i][0] = pow2[i]
for j in range(M+1):
    dp[0][j] = pow2[j]

# Fill DP table
for i in range(1, N+1):
    for j in range(1, M+1):
        dp[i][j] = (dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1] + pow2[min(i,j)]) % MOD

print(dp[N][M])

