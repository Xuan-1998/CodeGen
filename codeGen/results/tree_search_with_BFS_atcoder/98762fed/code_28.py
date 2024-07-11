MOD = 998244353
N, M = map(int, input().split())

fact = [1] * (N * M + 1)
inv = [1] * (N * M + 1)
for i in range(1, N * M + 1):
    fact[i] = fact[i - 1] * i % MOD
    inv[i] = pow(fact[i], MOD - 2, MOD)

def comb(n, k):
    if n < k or k < 0:
        return 0
    return fact[n] * inv[k] * inv[n - k] % MOD

dp = [[0] * (M + 1) for _ in range(N + 1)]
dp[0][0] = 1
for i in range(N + 1):
    for j in range(M + 1):
        if i + j == 0:
            continue
        dp[i][j] = (dp[i - 1][j] + dp[i][j - 1] - dp[i - 1][j - 1]) % MOD
        for k in range(1, min(i, j) + 1):
            dp[i][j] = (dp[i][j] + (comb(i * j, k) - comb((i - 1) * j, k) - comb(i * (j - 1), k) + 2 * MOD) * dp[i - k][j - k]) % MOD

print(dp[N][M])

