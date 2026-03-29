import sys

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_good_prime(n):
    prime_divisors = [i for i in range(2, n) if n % i == 0]
    return len(prime_divisors) == 1 and prime_divisors[0] != n

def beauty_value(arr):
    n = len(arr)
    dp = [[0] * (n + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        if is_prime(arr[i-1]):
            for j in range(i - 1, -1, -1):
                dp[j][i] = max(dp[j][i], (dp[j][i-1] if j > 0 else 0) + (1 if arr[i-1] % min(prime_divisors(arr[i-1])) != 1 and not is_good_prime(arr[i-1]) else 0))
        else:
            for j in range(i - 1, -1, -1):
                dp[j][i] = max(dp[j][i], (dp[j][i-1] if j > 0 else 0) + (1 if arr[i-1] % min(prime_divisors(arr[i-1])) != 1 and not is_good_prime(arr[i-1]) else 0))

    return dp[0][-1]

def prime_divisors(n):
    divisors = [i for i in range(2, int(n**0.5) + 1) if n % i == 0]
    if divisors:
        return min(divisors)
    return n

n, m = map(int, input().split())
arr = list(map(int, input().split()))
bad_primes = list(map(int, input().split()))

print(beauty_value(arr))
