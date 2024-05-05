import sys
from math import sqrt

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def min_prime_divisor(n):
    for p in range(2, int(sqrt(n)) + 1):
        if n % p == 0 and is_prime(p):
            return p
    return n

def beauty(arr, bad_primes):
    total_beauty = 0
    for num in arr:
        min_divisor = min_prime_divisor(num)
        if min_divisor in bad_primes:
            total_beauty += num * -1
        else:
            total_beauty += num * 1
    return total_beauty

n, m = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
bad_primes = list(map(int, sys.stdin.readline().split()))

print(beauty(arr, bad_primes))
