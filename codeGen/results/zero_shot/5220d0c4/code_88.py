import sys
from math import sqrt

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

n, m = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
bad_primes = list(map(int, sys.stdin.readline().split()))

max_beauty = 0
for num in arr:
    min_prime_divisor = None
    for prime in bad_primes:
        if is_prime(prime) and prime > sqrt(num):
            min_prime_divisor = prime
            break
    beauty = 1 if min_prime_divisor is None else -1 if is_prime(min_prime_divisor) else 0
    max_beauty = max(max_beauty, beauty)

print(max_beauty)
