a, b = map(int, input().split())
dp = [0] * 314160

for i in range(1, 314160):
    p = b >> (i % 2)
    dp[i] = (dp[i-1] + (a ^ p)) % (10**9+7)

print(dp[-1])
