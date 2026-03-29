import sys
from math import gcd

def f(s):
    p = min([i for i in range(2, int(s ** 0.5) + 1) if s % i == 0])
    if p not in bad_primes:
        return f(s // p) + s
    else:
        return f(s // p) - s

n, m = map(int, sys.stdin.readline().split())
a = list(map(int, sys.stdin.readline().split()))
bad_primes = set(map(int, sys.stdin.readline().split()))

max_beauty = 0
for num in a:
    while True:
        gcd_num = a[0]
        for i in range(1, n):
            gcd_num = gcd(gcd_num, a[i])
        if gcd_num == num:
            break
        else:
            a = [gcd(x, gcd_num) for x in a]
    max_beauty += f(num)

print(max_beauty)
