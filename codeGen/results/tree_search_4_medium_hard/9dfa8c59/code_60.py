from collections import Counter
from math import sqrt

def sieve_of_eratosthenes(n):
    sieve = [True] * (n+1)
    for x in range(2, int(sqrt(n)) + 1):
        if sieve[x]: 
            for i in range(x * x, n+1, x): 
                sieve[i] = False
    return [p for p in range(2, n) if sieve[p]]

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def get_permutations(n):
    counter = Counter(str(n))
    permutations = set()
    def permute(counter, current=""):
        if not counter:
            permutations.add(int(current or "0"))
            return
        for digit in counter:
            new_counter = counter.copy()
            new_counter[digit] -= 1
            if new_counter[digit] == 0:
                del new_counter[digit]
            permute(new_counter, current + digit)
    permute(counter)
    return len([p for p in permutations if is_prime(p)])

def solve():
    n_max, k_perms = map(int, input().split())
    primes_below_n = set(sieve_of_eratosthenes(n_max))
    count = 0
    min_prime = max_prime = None
    for prime in primes_below_n:
        if get_permutations(prime) == k_perms:
            count += 1
            min_prime = min(min_prime, prime) if min_prime else prime
            max_prime = max(max_prime, prime)
    print([count, min_prime, max_prime])

if __name__ == "__main__":
    solve()
