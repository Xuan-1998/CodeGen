import sys
from math import gcd

# Read input from stdin
n, m = map(int, sys.stdin.readline().split())
a = list(map(int, sys.stdin.readline().split()))
b = list(map(int, sys.stdin.readline().split()))

# Create a set of good prime numbers
good_primes = set()
for p in range(2, 10000):  # optimize this limit if needed
    is_prime = True
    for b_p in b:
        if p % b_p == 0:
            is_prime = False
            break
    if is_prime:
        good_primes.add(p)

# Define the beauty function f(s)
def beauty(s):
    if s <= 1:
        return 0
    min_prime = None
    for p in range(2, int(s ** 0.5) + 1):
        if s % p == 0 and p in good_primes:
            min_prime = p
            break
    if min_prime is not None:
        return beauty(s // min_prime) - s
    else:
        return beauty(s)

# Calculate the maximum beauty of the array
max_beauty = 0
for i in range(1, n + 1):
    max_beauty += beauty(a[i - 1])

print(max_beauty)
