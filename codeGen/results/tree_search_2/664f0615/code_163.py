import sys
from collections import defaultdict

memo = defaultdict(int)

def solve(v1, v2, t, delta):
    if v1 > v2:
        v1, v2 = v2, v1
    
    dp = [0] * (t + 1)
    
    for i in range(t + 1):
        for s in range(min(v1, v2) - max(0, delta), max(v2, v1) + min(delta, t)):
            if i == 0:
                continue
            dp[i] = max(dp[i], dp[i-1] + (s * 1))
    
    return dp[-1]

v1, v2 = map(int, input().split())
t, delta = map(int, input().split())

print(solve(v1, v2, t, delta))
