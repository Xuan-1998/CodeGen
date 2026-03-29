import math

def sieve_of_eratosthenes(n):
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False
    for i in range(2, int(math.sqrt(n)) + 1):
        if sieve[i]:
            for j in range(i * i, n + 1, i):
                sieve[j] = False
    return [p for p in range(2, n) if sieve[p]]

def min_prime_divisor(n):
    for p in range(2, int(math.sqrt(n)) + 1):
        if n % p == 0:
            return p

def beauty(arr, bad_primes):
    memo = {}
    def dp(i, k):
        if (i, k) in memo:
            return memo[(i, k)]
        if i >= len(arr):
            return 0
        if all(min_prime_divisor(x) not in bad_primes for x in arr[:i]):
            return 1 + dp(i - 1, k)
        best = 0
        for j in range(k, max(bad_primes)):
            if min_prime_divisor(arr[i]) <= j:
                best = max(best, dp(i - 1, j))
        memo[(i, k)] = best
        return best

    return dp(len(arr) - 1, max(bad_primes))

def main():
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    bad_primes = list(map(int, input().split()))
    print(beauty(arr, bad_primes))

if __name__ == "__main__":
    main()
