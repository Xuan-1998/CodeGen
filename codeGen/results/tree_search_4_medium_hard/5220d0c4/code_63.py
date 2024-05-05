import sys
from collections import defaultdict

def sieve_of_eratosthenes(n):
    primes = [True] * (n + 1)
    primes[0] = primes[1] = False
    for i in range(2, int(n ** 0.5) + 1):
        if primes[i]:
            for j in range(i * i, n + 1, i):
                primes[j] = False
    return [p for p in range(2, n + 1) if primes[p]]

def min_prime_divisor(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return i

def max_beauty(arr, bad_primes):
    n = len(arr)
    bad_primes_dict = {p: True for p in bad_primes}
    primes = set(sieve_of_eratosthenes(max(arr) + 1))
    dp = [[0, 0] for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        last_prime_divisor = min_prime_divisor(arr[i-1])
        if last_prime_divisor in bad_primes_dict:
            dp[i][0] = max(dp[i-1][0], dp[i-1][1])
            dp[i][1] = dp[i-1][0]
        else:
            dp[i][0] = max(dp[i-1][0], dp[i-1][1])
            dp[i][1] = max(dp[i-1][0], dp[i-1][1]) + 1
    
    return max(max(row) for row in dp)

if __name__ == "__main__":
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    bad_primes = list(map(int, input().split()))
    
    print(max_beauty(arr, bad_primes))
