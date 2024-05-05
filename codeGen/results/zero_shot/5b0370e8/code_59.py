import sys
from math import comb

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    res = (comb(2**k-1, n) % (10**9 + 7)) * 2**(k-n)
    print(res % (10**9 + 7))
