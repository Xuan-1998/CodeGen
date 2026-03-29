import sys
from math import gcd

def lcm(a, b):
    return a * b // gcd(a, b)

t = int(sys.stdin.readline())
for _ in range(t):
    n, k = map(int, sys.stdin.readline().split())
    and_res = 0
    xor_res = sum(1 for _ in range(n) if (1 << (k-1)) & int(input()))
    res = 0
    for i in range(k):
        bits = sum(1 for j in range(n) if (1 << i) & int(input()))
        and_res |= 1 << i if bits % 2 == 1 else 0
        xor_res ^= 1 << i if bits % 2 == 1 else 0
    res = pow(2, k - __builtin_popcount(and_res)) - 1
    print((res & xor_res) + (lcm(res, xor_res) // xor_res))
