import sys

def generate_primes(n):
    primes = [True] * (n + 1)
    primes[0] = primes[1] = False
    for i in range(2, int(n**0.5) + 1):
        if primes[i]:
            for j in range(i*i, n + 1, i):
                primes[j] = False
    return [i for i in range(2, n + 1) if primes[i]]

def calculate_beauty(arr, bad_primes):
    beauty = 0
    for num in arr:
        min_prime_divisor = None
        for prime in generate_primes(num):
            if num % prime == 0 and (prime not in bad_primes or num != prime):
                min_prime_divisor = prime
                break
        if min_prime_divisor is not None:
            if min_prime_divisor in bad_primes:
                beauty -= min_prime_divisor
            else:
                beauty += min_prime_divisor
    return beauty

n, m = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
bad_primes = list(map(int, sys.stdin.readline().split()))

print(calculate_beauty(arr, bad_primes))
