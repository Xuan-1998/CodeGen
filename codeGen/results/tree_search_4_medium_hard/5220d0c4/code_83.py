import sys

def max_beauty(n, m, arr, bad_primes):
    dp = [[0 for _ in range(m+1)] for _ in range(n+1)]

    for i in range(1, n+1):
        p = min(prime_divisors(arr[i-1]))
        if p in bad_primes:
            dp[i][m] -= p
        else:
            dp[i][m] += 1

    return max(dp[n])

def prime_divisors(n):
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            yield i
            while n % i == 0:
                n //= i
    if n > 1:
        yield n

n, m = map(int, input().split())
arr = list(map(int, input().split()))
bad_primes = list(map(int, input().split()))

print(max_beauty(n, m, arr, bad_primes))
