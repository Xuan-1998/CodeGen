import sys
from math import prod

n, m, h = map(int, input().split())
s = list(map(int, input().split()))
count = [0] * (m + 1)
for i in range(m):
    count[i+1] = sum(s[:i+1])

dp = [-1] * (n + 1)
dp[0] = 1
for i in range(1, n+1):
    if count[h] > 0:
        dp[i] = 1 - prod((count[j] / s for j in range(i))) * (1 - dp[i-1])
    else:
        dp[i] = -1

print(dp[n])  # Output the result
