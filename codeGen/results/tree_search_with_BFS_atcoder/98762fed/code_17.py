MOD = 998244353
N, M = map(int, input().split())

# precompute powers of 2 modulo MOD
pow2 = [1]*(N*M+1)
for i in range(1, N*M+1):
    pow2[i] = pow2[i-1]*2%MOD

# initialize dp array
dp = [[0]*(M+1) for _ in range(N+1)]
dp[0][0] = 1

# precompute prefix sums of dp array
prefix = [[0]*(M+1) for _ in range(N+1)]
prefix[0][0] = 1

for i in range(N+1):
    for j in range(M+1):
        if i > 0:
            prefix[i][j] += prefix[i-1][j]
        if j > 0:
            prefix[i][j] += prefix[i][j-1]
        if i > 0 and j > 0:
            prefix[i][j] -= prefix[i-1][j-1]
        prefix[i][j] %= MOD

# compute dp array
for i in range(1, N+1):
    for j in range(1, M+1):
        dp[i][j] = pow2[i*j]
        for a in range(1, i+1):
            for b in range(1, j+1):
                dp[i][j] -= dp[a-1][b-1]*pow2[(i-a+1)*(j-b+1)]
                dp[i][j] %= MOD

print(dp[N][M])

