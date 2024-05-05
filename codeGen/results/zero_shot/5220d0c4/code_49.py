import sys

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def beauty(num, bad_primes):
    prime_divisors = []
    for p in range(2, num):
        if is_prime(p) and num % p == 0:
            prime_divisors.append(p)
    min_prime_divisor = min(prime_divisors) if prime_divisors else 1
    return -1 if num in bad_primes else min_prime_divisor

n, m = map(int, sys.stdin.readline().split())
array = list(map(int, sys.stdin.readline().split()))
bad_primes = set(map(int, sys.stdin.readline().split()))

max_beauty = 0
for num in array:
    beauty_val = beauty(num, bad_primes)
    max_beauty = max(max_beauty, beauty_val)

print(max_beauty)
