import sys
from collections import defaultdict

mod = 10**9 + 7

def calcDP(i):
    if i not in memo:
        if i > 0 and (a & (1 << i)) == (b >> i) & 1:
            result = DP[i-1]
        else:
            result = a
        DP[i] = (result + ((b >> i) & 1)) % mod
    return DP[i]

memo = defaultdict(int)
DP = [0] * (10**5 + 1)

a, b = map(int, input().split())
for i in range(314160):
    calcDP(i)
print(sum(DP) % mod)
