import sys

def sieve_of_eratosthenes(n):
    primes = [True] * (n+1)
    primes[0] = primes[1] = False
    p = 2
    while p**2 <= n:
        if primes[p]:
            for i in range(p*p, n+1, p):
                primes[i] = False
        p += 1
    return [p for p in range(2, n+1) if primes[p]]

def max_beauty(arr, bad_primes):
    n = len(arr)
    dp = [[0]*n for _ in range(n)]
    sieve = sieve_of_eratosthenes(max(arr))
    
    def find_min_prime_divisor(x):
        i = 2
        while i <= x:
            if x % i == 0:
                return i
            i += 1
    
    for i in range(n-1, -1, -1):
        for j in range(i, n):
            min_prime_divisor = find_min_prime_divisor(arr[j])
            if min_prime_divisor not in bad_primes:
                dp[i][j] = max(dp[i][j], dp[i+1][j])
            else:
                dp[i][j] = 0
    
    return dp[0][n-1]

if __name__ == "__main__":
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    bad_primes = list(map(int, input().split()))
    print(max_beauty(arr, bad_primes))
