import sys

n = int(input())
s = input()

dp = [0] * (n + 1)
for i in range(n):
    dp[i+1] = dp[i]
    if s[i] == '1':
        for j in range(i+1, n+1):
            dp[j] = max(dp[j], dp[i] | ((j - i) << i))

print(bin(dp[-1])[2:].zfill(n).lstrip('0') or '0')
