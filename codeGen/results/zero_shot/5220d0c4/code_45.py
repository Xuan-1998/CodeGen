import sys

def sieve_of_eratosthenes(n):
    # Create a boolean array, prime, of size n+1
    prime = [True] * (n + 1)
    p = 2

    while p * p <= n:
        if prime[p]:
            for i in range(p * p, n + 1, p):
                prime[i] = False
        p += 1

    # Create a list of all bad primes
    bad_primes = []
    for p in range(2, n + 1):
        if prime[p]:
            bad_primes.append(p)

    return bad_primes


def find_min_prime_divisor(n, bad_primes):
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            if i in bad_primes:
                return i
            break

    if n > 1:
        return n


def calculate_beauty(array, bad_primes):
    beauty = 0
    for num in array:
        min_prime_divisor = find_min_prime_divisor(num, bad_primes)
        if min_prime_divisor in bad_primes:
            beauty -= 1
        else:
            beauty += 1

    return beauty


n, m = map(int, input().split())
array = list(map(int, input().split()))
bad_primes = list(map(int, input().split()))

print(calculate_beauty(array, bad_primes))
