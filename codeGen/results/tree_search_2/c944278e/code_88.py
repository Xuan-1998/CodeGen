import sys
from math import log2

n = int(input())
dp = [[False] * (1 << n) for _ in range(n)]

for i in range(n):
    s = int(input(), 2)
    for j in range(1 << n):
        if (j & s) == s:
            dp[i][j] = True

winners = []
for mask in range(1 << n):
    if any(dp[n-1][mask | m]):
        winners.append(mask)

print('\n'.join(map(lambda x: bin(x)[2:].zfill(n), sorted(winners))))
