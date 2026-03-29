import sys
from math import sqrt

def sieve_of_eratosthenes(n):
    # Create a boolean array, prime, of size n+1
    prime = [True] * (n + 1)
    prime[0] = prime[1] = False

    p = 2
    while p * p <= n:
        if prime[p]:
            for i in range(p * p, n + 1, p):
                prime[i] = False
        p += 1

    return [p for p in range(2, n + 1) if prime[p]]

def is_prime(n):
    # Check if a number is prime using the sieve of Eratosthenes
    return n > 1 and all(n % p for p in sieve_of_eratosthenes(int(sqrt(n))) + [n])

def max_beauty(arr, bad_primes):
    n = len(arr)
    m = len(bad_primes)

    # Create a 2D table to store the beauty values
    dp = [[0] * (m + 1) for _ in range(n)]

    # Fill the table from left to right, top to bottom
    for i in range(n):
        if is_prime(arr[i]):
            dp[i][0] = dp[i-1][1] + 1 if i > 0 else 1
        else:
            dp[i][0] = dp[i-1][0] if i > 0 else 0

    for j in range(m):
        dp[0][j+1] = 0

    for i in range(1, n):
        for j in range(min(i, m) + 1):
            if is_prime(arr[i]):
                dp[i][j+1] = max(dp[i-1][j], dp[i-1][j+1] + 1)
            else:
                dp[i][j+1] = max(dp[i-1][j], dp[i-1][j+1])

    # Return the maximum beauty value
    return max(dp[-1])

# Read input from standard input
n, m = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
bad_primes = list(map(int, sys.stdin.readline().split()))

# Print the output to standard output
print(max_beauty(arr, bad_primes))
