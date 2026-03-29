import sys
from math import sqrt

def sieve_of_eratosthenes(n):
    # Create a boolean array "prime[0..n]" and initialize all entries as true.
    # A value in prime[i] will finally be false if i is Not a prime, else true.
    prime = [True] * (n+1)
    p = 2
    while(p * p <= n):
        # If prime[p] is not changed, then it is a prime
        if prime[p]:
            for i in range(p * p, n+1, p):
                prime[i] = False
        p += 1

    bad_primes = set()
    good_primes = []

    while True:
        p = int(sys.stdin.readline())
        if p == -1:
            break
        bad_primes.add(p)

    array = list(map(int, sys.stdin.readline().split()))
    max_beauty = float('-inf')

    for num in array:
        is_prime = False
        for good_p in good_primes:
            if num % good_p != 0:
                is_prime = True
                break
        if not is_prime:
            continue

        min_divisor = num
        for p in range(2, int(sqrt(num)) + 1):
            if num % p == 0 and prime[p]:
                min_divisor = p
                break

        beauty = min_divisor
        for bad_p in bad_primes:
            if bad_p > min_divisor:
                beauty = max(beauty, bad_p)
                break

        max_beauty = max(max_beauty, beauty)

    print(max_beauty)
