import sys

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def beauty(num):
    prime = next((i for i in range(2, num) if is_prime(i) and num % i == 0), None)
    return -prime if is_prime(prime) else 0

n, m = map(int, input().split())
arr = list(map(int, input().split()))
bad_primes = list(map(int, input().split()))

dp = [0] * (n + 1)
memo = {}

for i in range(1, n + 1):
    if is_prime(arr[i - 1]):
        dp[i] = max(dp[i], dp[i - 1] + beauty(arr[i - 1]))
    else:
        dp[i] = max(dp[i], dp[i - 1] - 2)
    memo[dp[i]] = i

print(max(memo))
