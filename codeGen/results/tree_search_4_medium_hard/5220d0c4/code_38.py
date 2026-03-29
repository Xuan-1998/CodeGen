import sys

def sieve_of_eratosthenes(n):
    # Create a boolean array "prime[0..n]"
    prime = [True] * (n + 1)
    prime[0] = prime[1] = False
    p = 2
    while p**2 <= n:
        if prime[p]:
            for i in range(p**2, n + 1, p):
                prime[i] = False
        p += 1
    bad_primes = [i for i in range(2, n+1) if not prime[i]]
    return bad_primes

def max_beauty(n, m, arr, bad_primes):
    beauty = [[-1 for _ in range(n)] for _ in range(n)]
    dp = [[0 for _ in range(n)] for _ in range(2)]

    # Initialize the base cases
    for i in range(n):
        if i < m:
            dp[0][i] = 0
        else:
            good_primes = [p for p in range(i+1, n) if p not in bad_primes]
            dp[0][i] = max(0, sum(min(p-1, 2) for p in good_primes))

    # Fill the table using dynamic programming
    for length in range(1, n):
        for i in range(n-length):
            j = i + length
            if length < m:
                dp[1][j] = max(dp[0][k-1] + sum(min(p-1, 2) for p in [x for x in arr[i:j+1] if x not in bad_primes]), dp[1][j])
            else:
                dp[1][j] = max(dp[0][k-1] + sum(min(p-1, 2) for p in [x for x in arr[i:j+1] if x not in bad_primes]), dp[1][j])

    return max(beauty[i][n-1] for i in range(n))

# Read input from standard input
n, m = map(int, input().split())
arr = list(map(int, input().split()))
bad_primes = list(map(int, input().split()))

print(max_beauty(n, m, arr, bad_primes))
