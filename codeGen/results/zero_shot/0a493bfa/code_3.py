import sys
from math import gcd

def find_good_primes(bad_primes):
    good_primes = []
    for i in range(2, 109):
        is_good = True
        for p in bad_primes:
            if i % p == 0:
                is_good = False
                break
        if is_good:
            good_primes.append(i)
    return good_primes

def calculate_beauty(a, good_primes):
    beauty = 0
    while len(a) > 1:
        new_a = []
        for i in range(0, len(a)):
            gcd_val = a[0]
            for j in range(1, len(a)):
                gcd_val = gcd(gcd_val, a[j])
            new_a.append(gcd_val)
        a = new_a
    return beauty

def solve():
    n, m = map(int, sys.stdin.readline().split())
    a = list(map(int, sys.stdin.readline().split()))
    bad_primes = list(map(int, sys.stdin.readline().split()))
    good_primes = find_good_primes(bad_primes)
    print(calculate_beauty(a, good_primes))

solve()
