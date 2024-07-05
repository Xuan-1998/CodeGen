import math
import sys

def solve(n, a):
    if 1 in a:
        return n - a.count(1)
    else:
        min_gcd = float('inf')
        for i in range(n):
            for j in range(i+1, n):
                min_gcd = min(min_gcd, math.gcd(a[i], a[j]))
        if min_gcd == 1:
            return n - 1
        else:
            return -1

n = int(input().strip())
a = list(map(int, input().strip().split()))
print(solve(n, a))

