import sys
from math import sqrt

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

bad_primes = set()
n, m = map(int, sys.stdin.readline().split())
for _ in range(m):
    bad_primes.add(int(sys.stdin.readline()))

good_primes = [p for p in range(2, 110) if not is_prime(p) or p in bad_primes]

def f(s):
    p = min([p for p in good_primes if s % p == 0])
    return f(s // p) + s if is_prime(p) else f(s // p) - s

def max_beauty(a):
    if len(a) == 1:
        return f(a[0])
    max_b = 0
    for i in range(len(a)):
        new_a = a[:i] + [max_gcd(a[i], a[:i])]
        max_b = max(max_b, max_beauty(new_a))
    return max_b

def max_gcd(x, y):
    while y:
        x, y = y, x % y
    return x

print(max_beauty(list(map(int, sys.stdin.readline().split()))))
