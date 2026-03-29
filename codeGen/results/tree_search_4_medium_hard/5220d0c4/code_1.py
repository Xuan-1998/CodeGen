from collections import defaultdict
import math

def min_prime_divisor(n):
    if n % 2 == 0:
        return 2
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return i
    return n

def max_beauty(n, primes, memo = defaultdict(int)):
    for i in range(n+1):
        memo[(i, 0)] = i
    for p in primes:
        for i in range(p, n+1):
            if min_prime_divisor(i) <= p:
                memo[(i, p)] = max(memo.get((i-1, p), 0) + 1, memo.get((i, p-1), 0) - 1)
    return memo[(n, 0)]

# Read input
n, m = map(int, input().split())
arr = list(map(int, input().split()))
primes = list(map(int, input().split()))

print(max_beauty(n, primes))
