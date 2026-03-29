from collections import defaultdict

def sieve_of_eratosthenes(n):
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False
    for i in range(2, int(n ** 0.5) + 1):
        if sieve[i]:
            for j in range(i * i, n + 1, i):
                sieve[j] = False
    return [p for p in range(2, n + 1) if sieve[p]]

def min_prime_divisor(num):
    primes = sieve_of_eratosthenes(int(num ** 0.5) + 1)
    for prime in reversed(primes):
        if num % prime == 0:
            return prime
    return num

def max_beauty(arr, bad_primes):
    memo = defaultdict(int)
    memo[0] = 0

    def dp(i, prev_min_prime):
        if i >= len(arr) or arr[i] in bad_primes:
            return 0
        min_prime = min_prime_divisor(arr[i])
        if min_prime == prev_min_prime:
            return max(memo[i - 1], prev_min_prime + 1)
        else:
            for j in range(i):
                if arr[j] not in bad_primes and min_prime != min_prime_divisor(arr[j]):
                    return max(dp(j, min_prime), dp(i - 1, prev_min_prime))
            return 0

    return max(0, dp(len(arr) - 1, 0))

n, m = map(int, input().split())
arr = list(map(int, input().split()))
bad_primes = list(map(int, input().split()))

print(max_beauty(arr, bad_primes))
