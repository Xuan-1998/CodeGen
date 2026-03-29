import sys

def find_prime_divisors(n):
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False
    for i in range(2, int(n ** 0.5) + 1):
        if sieve[i]:
            for j in range(i * i, n + 1, i):
                sieve[j] = False
    return [i for i in range(2, n + 1) if sieve[i]]

def is_bad_prime(p, bad_primes):
    return p not in bad_primes

def max_beauty(n, array, bad_primes):
    prime_divisors = find_prime_divisors(max(array))
    beauty = 0
    for num in array:
        min_prime_divisor = min(prime_divisors[prime_divisors.index(num):])
        if is_bad_prime(min_prime_divisor, bad_primes):
            beauty -= 1
        else:
            beauty += 1
    return beauty

n, m = map(int, sys.stdin.readline().split())
array = list(map(int, sys.stdin.readline().split()))
bad_primes = list(map(int, sys.stdin.readline().split()))

print(max_beauty(n, array, bad_primes))
