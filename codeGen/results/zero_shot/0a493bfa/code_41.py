import sys
from math import gcd

# Read input
n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

# Find all prime numbers in the range [2, max(a)]
def is_prime(x):
    if x < 2:
        return False
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return False
    return True

primes = [x for x in range(2, max(a) + 1) if is_prime(x)]

# Mark bad prime numbers as "bad"
b_primes = [x for x in b if is_prime(x)]
for p in b_primes:
    primes.remove(p)

# Initialize the beauty of the array
b = 0

# Iterate through the array and perform operations
for i, x in enumerate(a):
    gcds = []
    for y in a[:i] + a[i+1:]:
        gcds.append(gcd(x, y))
    b += sum(1 if p in primes else -1 for p in gcds)

print(b)
