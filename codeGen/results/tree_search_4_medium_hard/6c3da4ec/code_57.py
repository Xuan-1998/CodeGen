import sys

n = int(input())
s = input()

dp = [0] * n
dp[0] = int(s[0], 2)

for i in range(1, n):
    if s[i] == '0':
        dp[i] = max(dp[i-1], dp[i-1] ^ 1)
    else:
        dp[i] = max(dp[i-1], dp[i-1] | 1)

print(bin(max(dp))[2:].zfill(n).lstrip('0') or '0')
