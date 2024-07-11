import sys
input = sys.stdin.readline

MOD = 998244353

def add(x, y):
    return (x + y) % MOD

def mul(x, y):
    return (x * y) % MOD

def power(x, y):
    if y == 0:
        return 1
    elif y % 2 == 0:
        return power(mul(x, x), y // 2)
    else:
        return mul(x, power(x, y - 1))

def inv(x):
    return power(x, MOD - 2)

def comb(n, r):
    if r < 0 or n < r:
        return 0
    return mul(fact[n], mul(inv_fact[r], inv_fact[n - r]))

N = int(input())
D = list(map(int, input().split()))

fact = [0] * (N + 1)
inv_fact = [0] * (N + 1)
fact[0] = 1
for i in range(1, N + 1):
    fact[i] = mul(fact[i - 1], i)
inv_fact[N] = inv(fact[N])
for i in range(N, 0, -1):
    inv_fact[i - 1] = mul(inv_fact[i], i)

dp = [[[0, 0] for _ in range(N + 1)] for _ in range(N + 1)]
dp[1][1][1] = 1
for i in range(2, N + 1):
    for j in range(1, i + 1):
        for k in range(i):
            dp[i][j][0] = add(dp[i][j][0], mul(dp[i - k][j - 1][0], mul(dp[k][D[k - 1]][1], comb(i - 1, k - 1))))
            dp[i][j][0] = add(dp[i][j][0], mul(dp[i - k][j - 1][1], mul(dp[k][D[k - 1]][0], comb(i - 1, k - 1))))
            dp[i][j][1] = add(dp[i][j][1], mul(dp[i - k][j][0], mul(dp[k][D[k - 1]][1], comb(i - 1, k))))
        dp[i][j][1] = add(dp[i][j][1], dp[i][j][0])

res = 0
for i in range(1, N + 1):
    res = add(res, dp[N][i][1])

print(res)

