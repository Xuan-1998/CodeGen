import sys
from math import sqrt

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

n, m = map(int, input().split())
arr = list(map(int, input().split()))
bad_primes = list(map(int, input().split()))

beauty = sum(1 for num in arr if not any(num % prime == 0 for prime in bad_primes) and is_prime(min(i for i in range(2, num + 1) if num % i == 0)))

print(beauty)
