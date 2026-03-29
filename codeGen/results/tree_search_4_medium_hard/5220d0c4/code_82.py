from collections import defaultdict

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def min_prime_divisor(n):
    for i in range(2, n + 1):
        if n % i == 0 and is_prime(i):
            return i
    return None

def max_beauty(n, bad_primes, arr):
    memo = defaultdict(int)
    dp = [[0] * (n + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(i, n + 1):
            if is_prime(min_prime_divisor(arr[j - 1])):
                dp[i][j] = max(dp[i][j - 1], arr[j - 1])
            else:
                dp[i][j] = dp[i][j - 1]
            for bad_prime in bad_primes:
                if bad_prime == min_prime_divisor(arr[j - 1]):
                    dp[i][j] -= arr[j - 1]

    return max(dp[1][n])

# Read input from stdin
n, m = map(int, input().split())
arr = list(map(int, input().split()))
bad_primes = list(map(int, input().split()))

print(max_beauty(n, bad_primes, arr))
