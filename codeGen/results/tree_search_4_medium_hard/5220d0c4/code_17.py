===BEGIN CODE===
import sys
from math import sqrt

def sieve_of_eratosthenes(n):
    primes = [True] * (n + 1)
    primes[0] = primes[1] = False
    for i in range(2, int(sqrt(n)) + 1):
        if primes[i]:
            for j in range(i*i, n+1, i):
                primes[j] = False
    return [p for p in range(2, n+1) if primes[p]]

def beauty(arr, bad_primes):
    n = len(arr)
    dp = [[0, 0] for _ in range(n + 1)]

    for i in range(1, n + 1):
        good_primes = [p for p in arr[i-1:] if p not in bad_primes]
        min_prime = min(good_primes) if good_primes else -1
        if min_prime == 0:
            dp[i][0] = len([p for p in arr[:i] if p not in bad_primes])
        else:
            dp[i][0] = max(dp[i-1][0], dp[i-1][1] + (min_prime == 2))

    for i in range(n, -1, -1):
        for j in range(2):
            dp[i][j] = max(dp[i][j], dp[i-1][0] if j else dp[i-1][1])

    return max(dp[n])

def main():
    n, m = map(int, sys.stdin.readline().split())
    arr = list(map(int, sys.stdin.readline().split()))
    bad_primes = list(map(int, sys.stdin.readline().split()))

    sieve = set(sieve_of_eratosthenes(max(arr) + 2))
    bad_primes = [p for p in bad_primes if p not in sieve]
    print(beauty(arr, bad_primes))

if __name__ == "__main__":
    main()
===END CODE===
