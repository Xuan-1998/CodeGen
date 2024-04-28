import sys

dp = [0] * (10**9 + 7)
a, b = map(int, input().split())
ans = 0

for i in range(315159):
    ans = (ans + dp[(b >> i) % (10**9 + 7)]) % (10**9 + 7)
    dp[b % (10**9 + 7)] = (dp[b % (10**9 + 7)] + a) % (10**9 + 7)

print(ans)
