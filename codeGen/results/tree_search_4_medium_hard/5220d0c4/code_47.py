def min_prime_divisor(n):
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return i
    return n

def beauty(arr, primes):
    dp = [0] * (len(arr) + 1)
    for i in reversed(range(len(arr))):
        min_prime = min_prime_divisor(arr[i])
        if arr[i] in primes:
            dp[i] = max(dp[i+1], dp[i-1] + min_prime if i > 0 else min_prime)
        else:
            dp[i] = max(0, dp[i+1] - 1)
    return dp[0]

n, m = map(int, input().split())
arr = list(map(int, input().split()))
primes = list(map(int, input().split()))

print(beauty(arr, primes))
