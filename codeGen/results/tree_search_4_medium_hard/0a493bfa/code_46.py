import math
from collections import defaultdict

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def beauty(arr, bad_primes):
    memo = defaultdict(int)
    max_beauty = [0] * (len(arr) + 1)

    def dp(i):
        if i in memo:
            return memo[i]
        if i == len(arr):
            return 0

        max_beauty[i] = max_beauty[i - 1]
        for j in range(i):
            g = gcd(arr[j], arr[i])
            if g not in bad_primes:
                max_beauty[i] = max(max_beauty[i], dp(j) + g)
            else:
                max_beauty[i] = max(max_beauty[i], dp(j) - g)

        memo[i] = max_beauty[i]
        return max_beauty[i]

    return max_beauty[-1]

# Read input
n, m = map(int, input().split())
arr = list(map(int, input().split()))
bad_primes = list(map(int, input().split()))

print(beauty(arr, bad_primes))
