import sys
from functools import reduce

# Read inputs from stdin
a = int(input())
b = int(input())

dp = [[0] * (314159 + 1) for _ in range(20)]

for i in range(20):
    dp[i][0] = 0

for i in range(19):
    for j in range(314160):
        if j >= 2**i:
            dp[i+1][j] = (dp[i][j-2**i] + a) % (10**9 + 7)
        else:
            dp[i+1][j] = dp[i][j]

ans = reduce(lambda x, y: (x + y) % (10**9 + 7), [dp[i][314159] for i in range(20)])

print(ans)
