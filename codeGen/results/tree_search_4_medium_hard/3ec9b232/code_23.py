import sys
from functools import lru_cache

@lru_cache(None)
def xor_partitions(i, p):
    if i == 0:
        return 1
    if p[i-1] == '0':
        return xor_partitions(i-1, p)
    else:
        return (xor_partitions(i-1, p^2) + 1) % (10**9+7)

n = int(input())
p = [int(x) for x in input().split()]

dp = [0]
for i in range(n):
    dp.append(dp[i] if p[i-1] == '0' else xor_partitions(i, p))

print(sum(dp) % (10**9+7))
