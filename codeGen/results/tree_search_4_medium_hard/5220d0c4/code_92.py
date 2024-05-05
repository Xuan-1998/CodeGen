import sys

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def min_prime_divisor(n):
    for p in range(2, int(n ** 0.5) + 1):
        if n % p == 0:
            return p
    return n

def beauty(n, is_good):
    if n <= 1:
        return 0
    prime = min_prime_divisor(n)
    return (prime > 2 and not is_good) or is_good

n, m = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
bad_primes = list(map(int, sys.stdin.readline().split()))

dp = [[0] * (m + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, min(i, m) + 1):
        prime = min_prime_divisor(arr[i - 1])
        dp[i][j] = max(dp[i - 1][j], beauty(arr[i - 1], is_good := not any(p == arr[i - 1] for p in bad_primes)))

print(max(dp[n]))
