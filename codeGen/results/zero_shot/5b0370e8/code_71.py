import sys
from math import log2

def count_arrays(n, k):
    total_and = 0
    for i in range(2**k):
        and_result = i & (i >> 1)
        total_and += and_result == 0
    return total_and % (10**9 + 7)

t = int(sys.stdin.readline())
for _ in range(t):
    n, k = map(int, sys.stdin.readline().split())
    print(count_arrays(n, k))
