import sys

def sieve_of_eratosthenes(n):
    # Generate all primes up to n
    primes = [True] * (n + 1)
    primes[0] = primes[1] = False
    for i in range(2, int(n ** 0.5) + 1):
        if primes[i]:
            for j in range(i * i, n + 1, i):
                primes[j] = False
    return [p for p in range(2, n + 1) if primes[p]]

def beauty(arr, bad_primes):
    max_beauty = 0
    for subset in itertoolschain(*[combinations(arr, r) for r in range(len(arr) + 1)]):
        beauty_score = 0
        for num in subset:
            prime_divisors = [p for p in sieve_of_eratosthenes(num) if num % p == 0]
            min_prime_divisor = min(prime_divisors)
            if min_prime_divisor in bad_primes:
                beauty_score -= min_prime_divisor
            else:
                beauty_score += min_prime_divisor
        max_beauty = max(max_beauty, beauty_score)
    return max_beauty

# Read input from stdin
n, m = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
bad_primes = list(map(int, sys.stdin.readline().split()))

# Calculate and print the maximum beauty
print(beauty(arr, bad_primes))
