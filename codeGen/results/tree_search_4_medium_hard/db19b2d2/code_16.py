import sys
from math import comb

def solve():
    n, m, h = map(int, input().split())
    s = list(map(int, input().split()))
    
    dp = [0] * (n + 1)
    dp[n] = 1 if sum(1 for i in range(m) if i == h and s[i]) >= h else 0
    
    for i in range(n - 1, 0, -1):
        dp[i] = comb(sum(s), n - i) / comb(sum(s), n)
    
    return 1 - sum(dp[:n+1])

print(solve())
