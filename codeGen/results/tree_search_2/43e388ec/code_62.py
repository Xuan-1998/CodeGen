import sys

mod = 10**9 + 7
dp = [[0] * 315160 for _ in range(2)]

def update_state(a, b, i):
    if a == 0:
        return dp[1][i-1]
    elif b == 0:
        return dp[0][i-1]
    else:
        return (dp[0][i-1] + dp[1][i-1]) % mod

a, b = map(int, input().split())
ans = 0
for i in range(314160):
    if a & 1 and b & 1:
        ans += update_state(a, b, i)
        ans %= mod
    a >>= 1
    b >>= 1
print(ans)
