import sys
import math

n, m = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
bad_primes = set(map(int, sys.stdin.readline().split()))

def f(s, bad_primes):
    if s == 1:
        return 0
    p = min((i for i in range(2, int(math.sqrt(s)) + 1) if s % i == 0), default=None)
    if p not in bad_primes:
        return f(s // p, bad_primes) + s
    else:
        return f(s // p, bad_primes) - s

def calculate_beauty(arr):
    beauty = 0
    for num in arr:
        beauty += f(num, bad_primes)
    return beauty

def max_beauty(n, m, arr, bad_primes):
    dp = [0] * (n + 1)
    for i in range(1, n + 1):
        beauty = calculate_beauty(arr[:i])
        dp[i] = max(dp[i - 1], beauty)
    return dp[-1]

print(max_beauty(n, m, arr, bad_primes))
