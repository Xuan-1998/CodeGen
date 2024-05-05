import sys
from math import comb

def solve(n, m, h):
    P = [0] * (n + 1)
    P[n-1] = 1 if h > 0 else 0
    
    for k in range(n-2, -1, -1):
        for i in range(min(k+1, h)+1):
            P[k] += comb(h, i) / comb(n-k, i)
    
    return P[0]

n, m, h = map(int, input().split())
print(solve(n, m, h))
