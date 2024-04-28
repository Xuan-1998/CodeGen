import sys
from math import gcd

n, k = map(int, input().split())

dp = [0] * (k + 1)
for i in range(1, n+1):
    for j in range(i, -1, -1):
        if gcd(j, k) == 1:
            dp[i] += dp[j-1]
            break

print((dp[k] % 1000000007))
