import sys
from collections import defaultdict

def solve():
    MOD = 10**9 + 7
    dp = [defaultdict(int) for _ in range(MOD)]
    
    for n, k in [list(map(int, input().split())) for _ in range(int(input()))]:
        for i in range(n):
            bit = bin(int(input()) & (2**k - 1))[2:].count('1')
            dp[bit % MOD][i] += 1

    ans = 0
    for d in dp:
        ans = (ans + sum(1 for v in d.values() if k := len(v) and all(x <= y for x, y in zip(range(k), v))):
    return str(ans % MOD)

print(solve())
