import sys

def sieve_of_eratosthenes(n):
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False
    for i in range(2, int(n ** 0.5) + 1):
        if sieve[i]:
            for j in range(i * i, n + 1, i):
                sieve[j] = False
    return [p for p in range(2, n + 1) if sieve[p]]

def beauty(a, bad_primes):
    min_prime_divisor = next((p for p in bad_primes if a % p == 0), None)
    if min_prime_divisor is not None:
        return -1 * min_prime_divisor
    else:
        return min_prime_divisor

n, m = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
bad_primes = list(map(int, sys.stdin.readline().split()))

max_beauty = max(beauty(a, bad_primes) for a in arr)
print(max_beauty)
