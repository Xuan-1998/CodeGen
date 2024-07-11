MOD = 998244353
N = int(input().strip())
d = list(map(int, input().strip().split()))

# Precompute the factorial and inverse factorial arrays
fac = [1] * (N+1)
inv = [1] * (N+1)
for i in range(1, N+1):
    fac[i] = fac[i-1] * i % MOD
    inv[i] = pow(fac[i], MOD-2, MOD)

# Initialize the DP table
dp = [[0] * (N+1) for _ in range(N+1)]
dp[0][0] = 1

# Compute the DP table
for i in range(1, N+1):
    for j in range(i, -1, -1):
        for k in range(j):
            dp[i][j] += dp[i-1][k] * fac[j] % MOD * inv[j-k] % MOD
            dp[i][j] %= MOD

# Compute the answer
ans = 0
for i in range(1, N+1):
    for j in range(1, i+1):
        ans += dp[i][j] * fac[N-1] % MOD * inv[i-1] % MOD * inv[N-i] % MOD * pow(2, N-i, MOD) % MOD
        ans %= MOD

print(ans)

