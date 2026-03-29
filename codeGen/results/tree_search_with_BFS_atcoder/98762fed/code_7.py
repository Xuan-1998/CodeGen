MOD = 998244353
N, M = map(int, input().split())
fact = [1] * 805
inv = [1] * 805
invfact = [1] * 805
for i in range(1, 805):
    fact[i] = fact[i - 1] * i % MOD
    inv[i] = MOD - MOD // i * inv[MOD % i] % MOD
    invfact[i] = invfact[i - 1] * inv[i] % MOD
C = lambda a, b: 0 if a < b else fact[a] * invfact[b] * invfact[a - b] % MOD
dp = [[0] * 405 for _ in range(405)]
dp[0][0] = 1
for i in range(N + 1):
    for j in range(M + 1):
        if i:
            dp[i][j] += dp[i - 1][j] * C(i + j - 1, i - 1) % MOD
        if j:
            dp[i][j] += dp[i][j - 1] * C(i + j - 1, j - 1) % MOD
        dp[i][j] %= MOD
print(dp[N][M])

