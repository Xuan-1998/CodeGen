import sys
from collections import defaultdict

def count_prime_permutations(n):
    if n < 10:
        return [True, True]
    count = 0
    primes = set()
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            continue
        j = i * i
        while j <= n:
            if not is_prime(j):
                break
            count += 1
            primes.add(int(str(j)))
            j += i
    return [len(primes), min(primes) if primes else -1, max(primes) if primes else -1]


def main():
    n_max = int(input())
    k_perms = int(input())
    print(*count_prime_permutations(n_max))


if __name__ == "__main__":
    main()
