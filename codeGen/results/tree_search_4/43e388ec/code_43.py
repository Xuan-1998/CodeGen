import sys

mod = 10**9 + 7

a, b = map(int, input().split())
dp = [[0] * (b + 1) for _ in range(a + 1)]

for i in range(b + 1):
    dp[0][i] = pow(2, i, mod)

for i in range(a + 1):
    dp[i][0] = 0

for i in range(1, a + 1):
    for j in range(1, b + 1):
        dp[i][j] = (dp[i-1][j-1] + ((a >> i) ^ (b >> j)) % mod)

ans = sum(dp[a][i] for i in range(b + 1))
print(ans)
