import sys

n = int(input())
s = input().strip()

dp = {0: 0}

max_or = 0
for i in range(1, n):
    dp[i] = max(dp.get(j-1, 0) << (i-j) for j in range(i+1))
    max_or = max(max_or, int(s[:i], 2) | dp[i])

print(bin(max_or)[2:].zfill(n).lstrip('0'))
