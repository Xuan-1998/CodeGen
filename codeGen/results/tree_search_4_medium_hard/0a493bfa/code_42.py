import math

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def solve():
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    bad_primes = list(map(int, input().split()))

    dp = [0] * (n + 1)
    for i in range(1, n + 1):
        for j in range(i):
            if arr[i - 1] not in bad_primes:
                g = gcd(arr[i - 1], arr[j])
                dp[i] = max(dp[i], dp[j] + g)

    return dp[n]

print(solve())
