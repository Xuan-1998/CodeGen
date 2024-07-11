MOD = 998244353
N, M = map(int, input().split())
MAX = max(N, M) + 1

# precalculate factorial and inverse factorial
fact = [1] * MAX
invfact = [1] * MAX
for i in range(1, MAX):
    fact[i] = (fact[i - 1] * i) % MOD
    invfact[i] = pow(fact[i], MOD - 2, MOD)

def C(n, k):
    if k < 0 or k > n: return 0
    return (fact[n] * invfact[k] * invfact[n - k]) % MOD

dp = [[0] * (M + 1) for _ in range(N + 1)]
dp[0][0] = 1
for i in range(N + 1):
    for j in range(M + 1):
        if i == 0 and j == 0: continue
        for k in range(i):
            for l in range(j):
                dp[i][j] = (dp[i][j] + dp[k][l] * C(i, k) * C(j, l)) % MOD

print(dp[N][M])

