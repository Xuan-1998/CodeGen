import sys

def sieve_of_eratosthenes(n):
    # Create a boolean array, prime, of size n+1
    prime = [True] * (n + 1)
    p = 2
    while p ** 2 <= n:
        if prime[p]:
            for i in range(p ** 2, n + 1, p):
                prime[i] = False
        p += 1

    # Store all prime numbers in the array primes
    primes = [p for p in range(2, n + 1) if prime[p]]

    return primes

def max_beauty(n, arr, bad_primes):
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    good_primes = set(sieve_of_eratosthenes(max(arr)))

    for i in range(1, n + 1):
        for j in range(i, n + 1):
            if arr[j - 1] in good_primes:
                dp[i][j] = max(dp[i][j - 1], dp[i - 1][j - 1] + min(good_primes))
            else:
                dp[i][j] = max(dp[i][j - 1], dp[i - 1][j - 1] - bad_primes[0])
    return dp[-1][-1]

if __name__ == "__main__":
    n, m = map(int, sys.stdin.readline().strip().split())
    arr = list(map(int, sys.stdin.readline().strip().split()))
    bad_primes = list(map(int, sys.stdin.readline().strip().split()))

    print(max_beauty(n, arr, bad_primes))
