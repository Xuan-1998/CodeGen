from collections import defaultdict

def max_beauty(n, m, arr, bad_primes):
    dp = [0] * (n + 1)
    for i in range(1, n + 1):
        if arr[i - 1] in bad_primes:
            dp[i] = min(dp[i - 1], n - 1)
        else:
            dp[i] = dp[i - 1] + 1
    return max(dp)

n, m = map(int, input().split())
arr = list(map(int, input().split()))
bad_primes = list(map(int, input().split()))

print(max_beauty(n, m, arr, bad_primes))
