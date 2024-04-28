def left_shift(b, i):
    return (b << i)

def xor(a, b):
    return a ^ b

MOD = 10**9 + 7

a, b = map(int, input().split())
dp = [[0] * 316 for _ in range(32)]

for i in range(32):
    dp[i][0] = xor(a, left_shift(b, i))
for i in range(1, 32):
    for j in range(i+1):
        if i - j >= 0:
            dp[i][j] = (dp[i-1][j] + dp[i-1][i-j]) % MOD

ans = sum(dp[31][i] for i in range(31))
print(ans)
