import sys

def sieve_of_eratosthenes(n):
    primes = [True] * (n + 1)
    primes[0] = primes[1] = False
    for i in range(2, int(n ** 0.5) + 1):
        if primes[i]:
            for j in range(i * i, n + 1, i):
                primes[j] = False
    return [p for p in range(2, n + 1) if primes[p]]

def max_beauty(A, bad_primes):
    n = len(A)
    dp = [[False] * (n - 1) for _ in range(n)]

    # Initialize the base case
    for i in range(n - 1):
        if all(p not in bad_primes for p in sieve_of_eratosthenes(A[i])):
            dp[0][i] = True

    for length in range(2, n):
        for i in range(n - length):
            j = i + length
            for k in range(i + 1, j):
                if all(p not in bad_primes for p in sieve_of_eratosthenes(A[k])):
                    dp[i][j] = max(dp[i][k], dp[k][j])

    # Return the maximum beauty value
    return int(any(dp[0][i] for i in range(n - 1)))

# Read input from standard input
n, m = map(int, input().split())
A = list(map(int, input().split()))
bad_primes = list(map(int, input().split()))

print(max_beauty(A, bad_primes))
